from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    client = MongoClient(os.getenv("MONGODB_URI"))
    db = client["final_work"]
    events_collection = db["events"]


    @app.route("/month/<int:month_num>")
    def month_view(month_num):
        month_str = f"{month_num:02d}-"
        docs = events_collection.find({"date": {"$regex": f"^{month_str}"}})
        events = [(doc.get("date"), doc.get("event")) for doc in docs]
        return render_template("month.html", events=events)

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            date = request.form.get("date")
            event = request.form.get("event")

            try:
                date_obj = datetime.strptime(date, "%m-%d")
                events_collection.insert_one({
                    "date": date_obj.strftime("%m-%d"),
                    "event": event
                })
                return redirect(url_for('index'))
            except ValueError:
                return "Invalid date format. Use mm-dd."

        return render_template("index.html")


    @app.route("/statistics", methods=["GET", "POST"])
    def statistics():
        if request.method == "POST":
            date_str = request.form.get("date")
            try:
                input_date = datetime.strptime(date_str, "%m-%d")
                current_year = datetime.now().year
                input_date = input_date.replace(year=current_year)
                stats = calculate_statistics(events_collection, input_date)
                return render_template("statistics.html", stats=stats, input_date=date_str)
            except ValueError:
                return "Invalid date format. Use mm-dd."

        return render_template("statistics.html", stats=None)

    return app

def calculate_statistics(events_collection, input_date):
    start_date = datetime(input_date.year, 1, 1)
    events_from_start = events_collection.count_documents(
        {"date": {"$gte": start_date.strftime("%m-%d"), "$lte": input_date.strftime("%m-%d")}})
    events_on_date = list(events_collection.find({"date": input_date.strftime("%m-%d")}))
    past_events = list(events_collection.find({"date": {"$lt": input_date.strftime("%m-%d")}}).sort("date", 1))
    future_events = list(events_collection.find({"date": {"$gte": input_date.strftime("%m-%d")}}).sort("date", 1))

    return {
        "events_from_start": events_from_start,
        "events_on_date": events_on_date,
        "past_events": past_events,
        "future_events": future_events
    }

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
