# """Heavy task functions for load simulation (CPU, JSON, hashing)."""

# import hashlib
# from flask import jsonify


# def calc_cpu():
#     """Performs a CPU-intensive calculation."""
#     return str(sum(i * i for i in range(10**7)))


# def calc_hash():
#     """Generates SHA-256 hashes to simulate CPU load."""
#     data = b"EDP load test"
#     for _ in range(10**5):
#         hashlib.sha256(data).hexdigest()
#     return "Hashing complete"


# def generate_json():
#     """Generates a large JSON payload."""
#     payload = [{"id": i, "value": i * i} for i in range(100000)]
#     return jsonify(payload)
