import json
import logging
import urllib.request


logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    logger.debug(event)
    
    
    if event["currentIntent"]["name"]=='SLOT_NAME_FOR_LOCATION':
        global city
        city=event["currentIntent"]["slots"]["Location"]
        message="What do you want to look for? Try giving me commands like: temperature,pressure,humidity, or condition"
        
        return {
          "sessionAttributes": event["sessionAttributes"],
          "dialogAction": {
                "type": "ElicitSlot",
                "intentName":"GetWeather",
                "slotToElicit":"choice",
                "message":{
                    "contentType":"PlainText",
                    "content":message
                    
            }
        }
    }
    elif event["currentIntent"]["name"]=="SLOT_NAME_FOR_WEATHER":
        
        choice=event["currentIntent"]["slots"]["choice"]
        
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        API_KEY = "e914e5e16947fe541140de82a88e5888"
        URL = BASE_URL + "q=" + city + "&appid=" + API_KEY
        
        response = json.load(urllib.request.urlopen(URL))
        
        if response['cod'] == 200:
    	    main = response['main']
    	    temperature = '{:.2f}'.format(main['temp']-273.15)
    	    min_temp='{:.2f}'.format(main['temp_min']-273.15)
    	    max_temp='{:.2f}'.format(main['temp_max']-273.15)
    	    humidity = main['humidity']
    	    pressure = main['pressure']
    	    report = response['weather']
    	    
        if choice=="temperature":
            
            message=f"The Temperature of {city} is {temperature}°C. \n The maximum temperature will be {max_temp}°C and minimum will be {min_temp}°C."
            return {
                "sessionAttributes": event["sessionAttributes"],
                "dialogAction": {
                    "type": "ElicitSlot",
                    "intentName":"GetWeather",
                    "slotToElicit":"choice",
                    "message":{
                        "contentType":"PlainText",
                        "content":message
                    
            }
        }
    }
                
        if choice=="humidity":
            message=f"The Humidity of {city} is {humidity}%."
            return {
                "sessionAttributes": event["sessionAttributes"],
                "dialogAction": {
                    "type": "ElicitSlot",
                    "intentName":"GetWeather",
                    "slotToElicit":"choice",
                    "message":{
                        "contentType":"PlainText",
                        "content":message
                    
            }
        }
    }
                
        if choice=="pressure":
            message=f"The Pressure of {city} is {pressure}."
            return {
                "sessionAttributes": event["sessionAttributes"],
                "dialogAction": {
                    "type": "ElicitSlot",
                    "intentName":"GetWeather",
                    "slotToElicit":"choice",
                    "message":{
                        "contentType":"PlainText",
                        "content":message
                        }
                    
                }
                
            }
                        
        if choice=="condition":
            message = f"The weather report of {city} is {report[0]['description']}."
            return {
                "sessionAttributes": event["sessionAttributes"],
                "dialogAction": {
                    "type": "ElicitSlot",
                    "intentName":"GetWeather",
                    "slotToElicit":"choice",
                    "message":{
                        "contentType":"PlainText",
                        "content":message
                    
            }
        }
    }
    
        if choice=='done':
            message ="Thank you for using our service."
            return {
                "sessionAttributes": event["sessionAttributes"],
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState":"Fulfilled",
                    "message":{
                        "contentType":"PlainText",
                        "content":message
                    
            }
        }
    }
    
