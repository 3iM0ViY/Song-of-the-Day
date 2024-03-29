from ytmusicapi import YTMusic
import pprint
import cgi

yt = YTMusic('oauth.json')
search_results = yt.search('The Gateway', filter="songs")
for result in search_results:
	# if result['category'] == 'Songs' and result['resultType'] == "song":
	pprint.pp(result)

# meta = yt.get_watch_playlist("The Gateway")
# print(meta)
# print(yt.get_lyrics('0FM3lsVsznM'))

cgitb.enable()