import python_weather, asyncio, os

# ripped straight from documentation since there isn't real documentation. editing later
# https://pypi.org/project/python-weather/
async def getweather(location):
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(location)
        forecasts = {}
        for forecast in weather.forecasts:
            forecasts.update(forecast.date, forecast.astronomy)
        w_details = {
            "curr_temp":weather.current.temperature,
            "forecasts":forecasts
        }
        return w_details

# bugfix for asyncio client
# https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
if __name__ == "__main__":
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    asyncio.run(getweather())