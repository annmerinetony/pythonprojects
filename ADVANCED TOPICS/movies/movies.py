import json
def get_data():
    with open("movies.json",encoding="utf8") as f:
        return json.load(f)

class Movies:
    def get(self):
        data=get_data()
        return[ movie["title"] for movie in data]
movie=Movies()
print(movie.get())

# class MovieyearFilter:
#     def get(self,start_year,end_year):
#         data=get_data()
#         mvs=[movie for movie in data if movie["year"] in range(start_year,(end_year+1))]
#         return mvs


class MovieyearFilter:
    def get(self,**kwargs):
        data=get_data()
        st_year=kwargs.get("start_year")
        en_year=kwargs.get("end_year")
        mvs=[movie for movie in data if movie["year"] in range(st_year,(en_year+1))]
        return mvs
myf=MovieyearFilter()
print(myf.get(start_year=2015,end_year=2016))

class MovieGeneresFilter:
    def get(self,**kwargs):
        gener=kwargs.get("genres")
        data = get_data()
        return [m for m in data if gener in m["genres"]]

mgf=MovieGeneresFilter()
print(mgf.get(genres="Action"))

class MovieFilter():
    def get(self,**kwargs):
        gener = kwargs.get("genres")
        yr=kwargs.get("year")
        data = get_data()

        return [m for m in data if m["year"]==yr and gener in m["genres"]]
mf= MovieFilter()
mf.get(year=2017,genres="Action")
