import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "H7uYHxGVsuxCNjJPKpukTX19qYWvxh4G"

while True:
    orig = input("Indique la ciudad de origen: ")
    if orig == "salir" or orig == "s":
        break
    dest = input("Indique la ciudad de destino: ")
    if dest == "salir" or orig == "s":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    print("=============================================\n")
    if json_status == 0:
        distance_km = round(json_data["route"]["distance"] * 1.61, 2)
        duration = json_data["route"]["formattedTime"]
        print("La distancia entre ciudades esde: {:.1f}".format(distance_km),"km")
        print("La duracion del viaje es de: " + duration,"hrs\n")
        print("=============================================\n")
        print("Indicaciones de como llegar:\n")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.1f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

