import csv
from flask import Flask, jsonify, request

app = Flask(__name__)

# Specify the path to your CSV file
csv_file_path = r'C:\Users\ramad\PycharmProjects\HackerRankAutomation\HR_Result_data.csv'

@app.route('/api/hackerrankdata', methods=['GET', 'POST'])
def hackerrank_data():
    if request.method == 'GET':
        # Read data from CSV file and return as JSON
        hackerrankdata = []
        with open(csv_file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                hackerrankdata.append(dict(row))
        return jsonify(hackerrankdata)

    elif request.method == 'POST':
        # Insert new data into CSV file
        try:
            new_data = request.json
            with open(csv_file_path, 'a', newline='') as csvfile:
                fieldnames = ["Accuracy", "Difficulty", "Max_Score", "Problem status"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Write header if the file is empty
                if csvfile.tell() == 0:
                    writer.writeheader()

                # Write new data to CSV
                writer.writerow(new_data)

            return jsonify({"message": "Data added successfully"}), 201

        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
