"""
Project Name : Performance Load Testing
Internship   : CodeTech IT Solutions

This program performs a basic load test on a website by
sending multiple HTTP GET requests and measuring the
response time for each request.
"""

import requests
import time

# -------------------------------
# Configuration
# -------------------------------
URL = "https://example.com"
TOTAL_REQUESTS = 10

print("=" * 50)
print("        PERFORMANCE LOAD TEST")
print("=" * 50)

response_times = []
successful_requests = 0

for i in range(1, TOTAL_REQUESTS + 1):

    try:
        start = time.time()

        response = requests.get(URL)

        end = time.time()

        elapsed = end - start

        response_times.append(elapsed)
        successful_requests += 1

        print(
            f"Request {i:02d} | "
            f"Status: {response.status_code} | "
            f"Response Time: {elapsed:.3f} sec"
        )

    except Exception as e:
        print(f"Request {i:02d} Failed : {e}")

# -------------------------------
# Summary
# -------------------------------
print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)

if response_times:

    average = sum(response_times) / len(response_times)

    print("Website              :", URL)
    print("Total Requests       :", TOTAL_REQUESTS)
    print("Successful Requests  :", successful_requests)
    print("Average Response Time:", round(average, 3), "seconds")

    with open("results.txt", "w") as file:
        file.write("Performance Load Test Results\n")
        file.write("-" * 40 + "\n")
        file.write(f"Website : {URL}\n")
        file.write(f"Total Requests : {TOTAL_REQUESTS}\n")
        file.write(f"Successful Requests : {successful_requests}\n")
        file.write(f"Average Response Time : {average:.3f} seconds\n")

print("\nResults saved in results.txt")