import base64

import camera
import machine
import ujson
import urequests
import utime


def main():
    url = 'http://75.145.230.89:5000/save'
    errr_count = 0
    camera.deinit()

    try:
        camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)  # ESP32-CAM
        print("camera ready")
        utime.sleep(1)
    except:
        utime.sleep(5)
        machine.reset()

    while True:
        try:
            print("looping")
            buf = camera.capture()
     
            img_byte = base64.b64encode(buf)
            utime.sleep(2)
            img_json = ujson.dumps({"image": img_byte})
            utime.sleep(2)
            res = urequests.post(url, data=img_json)
            print(res.text)
            utime.sleep(2)
        except:
            errr_count += 1
            print(errr_count)
            if errr_count == 10:
                # machine.reset()
                break


main()
