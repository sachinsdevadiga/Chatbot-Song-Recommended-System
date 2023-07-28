from lastfmpy import LastFM
import asyncio

API_KEY = "64210b6f3784f96bdd70c1dd393b5c7e"
# if it isn't obvious enough, replace this string 
# with your API key obtained by going to https://last.fm/api/applications and creating an application

async def main():
    lastfm = await LastFM(API_KEY)
    recent = await lastfm.user.get_recent_tracks(user="sakshimayya")
    print(f"{recent.items[0].name}")


asyncio.get_event_loop().run_until_complete(main())

