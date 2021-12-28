import os


@app.route("/")
def index():
    return render_template('index.html')
@app.route("/<deviceName>/")
def action(deviceName):
    if deviceName != 'monstermash':
        if deviceName == 'stonewolf':
            relay = stonewolf
        if deviceName == 'werewolf':
            relay = werewolf
        if deviceName == 'pumpkin':
            relay = pumpkin
        if deviceName == 'zombie':
            relay = zombie
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(relay, GPIO.OUT)
        GPIO.output(relay, GPIO.LOW)
        time.sleep(5)
        GPIO.output(relay, GPIO.HIGH)
    else:
        relay = monstermash
        for x in relay:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(x, GPIO.OUT)
            GPIO.output(x, GPIO.LOW)
        time.sleep(5)
        for x in relay:
            GPIO.output(x, GPIO.HIGH)
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
