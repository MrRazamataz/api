# api
An "API" that serves no proper purpose other than random tat

## Info:
Find the status of `api.mrrazamataz.ga` under "RazasVPS" [here](https://status.mrrazamataz.ga/).


## Endpoints:  

### yturl:  
`yturl` - Get the video URL of a video on YouTube with a search query.   
##### Params:
* `search` - search query
##### Example:
```
api.mrrazamataz.ga/yturl?search=song 2 blur
```
##### Response:
```json
{"error":"False","video_url":"https://www.youtube.com/watch?v=SSbBvKaM6sk"}
```