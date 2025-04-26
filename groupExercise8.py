from flask import Flask, request, jsonify

app = Flask(__name__)

datasets = {
    'customer_data': [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}],
    'sales_report': [{'month': 'April', 'sales': 10000}],
    'finance': [{'budget': 500000, 'expenses': 300000}]
}

Roles = {
    'admin': ['customer_data', 'sales_report', 'finance'],
    'analyst': ['sales_report'],
    'guest': []
}

users = {
    'admin_user': 'admin',
    'analyst_user': 'analyst',
    'guest_user': 'guest'
}

def get_user_role():
    username = request.headers.get('Username')
    if username and username in users:
        return users[username]
    return None

@app.route('/data/<dataset_name>', methods=['GET'])
def get_dataset(dataset_name):
    role = get_user_role()
    if not role:
        return jsonify({'error': 'Unauthorized user'}), 401
    
    allowed_datasets = Roles.get(role, [])
    if dataset_name not in allowed_datasets:
        return jsonify({'error': f'Access denied for role {role}'}), 403

    data = datasets.get(dataset_name)
    if data is None:
        return jsonify({'error': 'Dataset not found'}), 404

    return jsonify({'dataset': dataset_name, 'data': data})

if __name__ == '__main__':
    app.run(debug=True)
