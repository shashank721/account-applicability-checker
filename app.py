from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the Excel file into a pandas DataFrame
file_path = "data/accounts.xlsx"
data = pd.read_excel(file_path)
account_dict = data.set_index('account no')['is applicable'].to_dict()

@app.route('/check_applicability', methods=['GET'])
def check_applicability():
    account_no = request.args.get('account_no')
    if account_no in account_dict:
        is_applicable = account_dict[account_no]
        return jsonify({"applicable": is_applicable})
    else:
        return jsonify({"error": "Account number not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
