import time
from gpiozero import LightSensor, Buzzer, LED, Button
from signal import pause

ldr1 = LightSensor("GPIO26")
ldr2 = LightSensor("GPIO19")
ldr3 = LightSensor("GPIO13")
ldr4 = LightSensor("GPIO6")

led1 = LED(12)
button1 = Button(4)
led2 = LED(16)
button2 = Button(17)
led3 = LED(20)
button3 = Button(27)
led4 = LED(21)
button4 = Button(22)

led1.on()
led2.on()
led3.on()
led4.on()

while True:
    ldrlt = round(ldr1.value*1000) #top left  LDR
    ldrrt = round(ldr2.value*1000) #top rigt  LDR
    ldrld = round(ldr4.value*1000) #down left LDR
    ldrrd = round(ldr3.value*1000) #down rigt LDR

#buttons
    button1.when_pressed = led1.off
    button1.when_released = led1.on
    button2.when_pressed = led2.off
    button2.when_released = led2.on
    button3.when_pressed = led3.off
    button3.when_released = led3.on
    button4.when_pressed = led4.off
    button4.when_released = led4.on
#digital pins

    NS1 = led1 # NS1 = North-South + relay number + pin
    NS2 = led2 # NS2 = North-South + relay number + pin
    EW3 = led3 # EW3 = East-West + relay number + pin
    EW4 = led4 # EW4 = East-West + relay number + pin


    tol = 200 # tolerance between LDR readings

    avt = (ldrlt+ldrrt)/2 #// average value top
    avd = (ldrld+ldrrd)/2 #// average value down
    avl = (ldrlt+ldrld)/2 #// average value left
    avr = (ldrrt+ldrrd)/2 #// average value right

    dvert = avt - avd # // check the diffirence of up and down
    dhoriz = avl - avr #// check the diffirence og left and rigt

    if -tol>dvert or dvert>tol: #// check if the diffirence is in the tolerance else change vertical angle
                                # difference in vertical is great enough to act on
        if avt>avd: 
      #// avg resistance on top is greater than on bottom
            NS1.on()
            NS2.off()
        else:
      #// avg resistance on bottom is greater than on top
            NS2.on()
            NS1.off()
    
    else:
    #//difference in vertical is below tolerance
        NS1.on()
        NS2.on()
  
    if -tol>dhoriz or dhoriz>tol:
    #// difference in horizontal is great enough to act on
        if avl>avr:
        #// avg resistance on left is greater than on right
            EW3.on() 
            EW4.off()
        else:
        #// avg resistance on right is greater than on left
            EW4.on()
            EW3.off()
    else: 
    #//difference in horizontal is below tolerance
        EW3.on()
        EW4.on()
  
    #// Wait a second before checking again
    time.sleep(1)
