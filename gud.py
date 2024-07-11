import webbrowser, time 
url = input("Enter URL: ")
duration = input("Enter duration: ")
for i in range(10):
      webbrowser.open_new(url)
      time.sleep(int(duration))
