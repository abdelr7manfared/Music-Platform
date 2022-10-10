## create some artists
`
artist =  Artist(Stage_name='artist1', Social_link_field='https://www.instagram.com/artist1/')
artist.save()
artist =  Artist(Stage_name='artist2', Social_link_field='https://www.instagram.com/artist2/')
artist.save()
artist =  Artist(Stage_name='artist3', Social_link_field='https://www.instagram.com/artist3/')
artist.save()
artist =  Artist(Stage_name='artist4', Social_link_field='https://www.instagram.com/artist4/')
artist.save()
artist =  Artist(Stage_name='artist5', Social_link_field='https://www.instagram.com/artist5/')
artist.save()
`
## list down all artists
`Artist.objects.all()`
-----
`<QuerySet [<Artist: StageName:artist1 ,SocialLink: https://www.instagram.com/artist1/
>, <Artist: StageName:artist2 ,SocialLink: https://www.instagram.com/artist2/        
>, <Artist: StageName:artist3 ,SocialLink: https://www.instagram.com/artist3/
>, <Artist: StageName:artist4 ,SocialLink: https://www.instagram.com/artist4/
>, <Artist: StageName:artist5 ,SocialLink: https://www.instagram.com/artist5/
>, <Artist: StageName:artist6 ,SocialLink: https://www.instagram.com/artist6/
>]>`

## list down all artists sorted by name 
`Artist.objects.all().order_by('Stage_name')`
-----
`<QuerySet [
<Artist: StageName:artist1 ,SocialLink: https://www.instagram.com/artist1/>,
<Artist: StageName:artist2 ,SocialLink: https://www.instagram.com/artist2/>,
<Artist: StageName:artist3 ,SocialLink: https://www.instagram.com/artist3/>,
<Artist: StageName:artist4 ,SocialLink: https://www.instagram.com/artist4/>,
<Artist: StageName:artist5 ,SocialLink: https://www.instagram.com/artist5/>,
<Artist: StageName:artist6 ,SocialLink: https://www.instagram.com/artist6/>
]>
`
## list down all artists whose name starts with `a`
`Artist.objects.filter(Stage_name__startswith='a')`
-----
`<QuerySet [<Artist: StageName:artist1 ,SocialLink: https://www.instagram.com/artist1/
>, <Artist: StageName:artist2 ,SocialLink: https://www.instagram.com/artist2/
>, <Artist: StageName:artist3 ,SocialLink: https://www.instagram.com/artist3/
>, <Artist: StageName:artist4 ,SocialLink: https://www.instagram.com/artist4/
>, <Artist: StageName:artist5 ,SocialLink: https://www.instagram.com/artist5/
>, <Artist: StageName:artist6 ,SocialLink: https://www.instagram.com/artist6/
>]>`
## in 2 different ways, create some albums and assign them to any artists (hint: use `objects` manager and use the related object reference)
### first way 
`artist = Artist.objects.get(pk=2)`
`Album(name="LOL!",release_date=datetime.datetime(2007,11,19),cost=15.19,artist=artist)`
### second way 
`artist = Artist.objects.get(pk=5)`
`artist.album_set.create(name="help",release_date=datetime.datetime(2017,11,19),cost=125)`
#  get the latest released album
 `Album.objects.order_by('release_date').reverse()[0]`
 -----
`<Album: Name:hh,CreationDate:2022-10-07 09:00:33.362215+00:00,ReleaseDate:2205-01-01 00:00:00+00:00,Cost:8.00>`
## get all albums released before today
`Album.objects.filter(release_date__lt = timezone.now())
`
-----
`<QuerySet [<Album: Name:Help i lost!,CreationDate:1997-10-19 00:00:00+00:00,ReleaseDate:1997-10-19 00:00:00+00:00,Cost:15.19>, <Album: Name:Help i lost!,CreationDate:2022-10-07 07:52:25.818482+00:00,ReleaseDate:1997-10-19 00:00:00+00:00,Cost:15.19>, <Album: Name:LOL!,CreationDate:2022-10-07 07:53:36.946724+00:00,ReleaseDate:2007-11-19 00:00:00+00:00,Cost:15.19>, <Album: Name:lol pro,CreationDate:2022-10-07 08:56:05.430014+00:00,ReleaseDate:2005-01-01 00:00:00+00:00,Cost:12.00>, <Album: Name:lol pro,CreationDate:2022-10-07 09:00:21.770458+00:00,ReleaseDate:2005-01-01 00:00:00+00:00,Cost:12.00>, <Album: Name:help,CreationDate:2022-10-07 09:02:57.055218+00:00,ReleaseDate:2017-11-19 00:00:00+00:00,Cost:125.00>, <Album: Name:help,CreationDate:2022-10-07 09:03:09.210007+00:00,ReleaseDate:2017-11-19 00:00:00+00:00,Cost:125.00>]>`
## get all albums released today or before but not after today
`Album.objects.filter(release_date__lt = timezone.now())`
-----
`<QuerySet [<Album: Name:Help i lost!,CreationDate:1997-10-19 00:00:00+00:00,ReleaseDate:1997-10-19 00:00:00+00:00,Cost:15.19>, <Album: Name:Help i lost!,CreationDate:2022-10-07 07:52:25.818482+00:00,ReleaseDate:1997-10-19 00:00:00+00:00,Cost:15.19>, <Album: Name:LOL!,CreationDate:2022-10-07 07:53:36.946724+00:00,ReleaseDate:2007-11-19 00:00:00+00:00,Cost:15.19>, <Album: Name:lol pro,CreationDate:2022-10-07 08:56:05.430014+00:00,ReleaseDate:2005-01-01 00:00:00+00:00,Cost:12.00>, <Album: Name:lol pro,CreationDate:2022-10-07 09:00:21.770458+00:00,ReleaseDate:2005-01-01 00:00:00+00:00,Cost:12.00>, <Album: Name:help,CreationDate:2022-10-07 09:02:57.055218+00:00,ReleaseDate:2017-11-19 00:00:00+00:00,Cost:125.00>, <Album: Name:help,CreationDate:2022-10-07 09:03:09.210007+00:00,ReleaseDate:2017-11-19 00:00:00+00:00,Cost:125.00>]>`
## count the total number of albums (hint: count in an optimized manner)
`Album.objects.count()`
-----
`11`
## in 2 different ways, for each artist, list down all of his/her albums (hint: use `objects` manager and use the related object reference)
### first way 
`for art in Artist.objects.all():print(art,Album.objects.filter(artist=art.id))`
-----
`StageName:artist1 ,SocialLink: https://www.instagram.com/artist1/ <QuerySet [<Album: Name:Help i lost!,CreationDate:1997-10-19 00:00:00+00:00,ReleaseDate:1997-10-19 00:00:00+00:00,Cost:15.19>, <Album: Name:Help i lost!,CreationDate:2022-10-07 07:52:25.818482+00:00,ReleaseDate:1997-10-19 00:00:00+00:00,Cost:15.19>, <Album: Name:LOL!,CreationDate:2022-10-07 07:53:36.946724+00:00,ReleaseDate:2007-11-19 00:00:00+00:00,Cost:15.19>, <Album: Name:lol pro,CreationDate:2022-10-07 08:56:05.430014+00:00,ReleaseDate:2005-01-01 00:00:00+00:00,Cost:12.00>, <Album: Name:lol pro,CreationDate:2022-10-07 09:00:21.770458+00:00,ReleaseDate:2005-01-01 00:00:00+00:00,Cost:12.00>, <Album: Name:hh,CreationDate:2022-10-07 09:00:59.419060+00:00,ReleaseDate:2205-01-01 00:00:00+00:00,Cost:8.00>]>
StageName:artist2 ,SocialLink: https://www.instagram.com/artist2/ <QuerySet [<Album: Name:hh,CreationDate:2022-10-07 09:01:10.605074+00:00,ReleaseDate:2205-01-01 00:00:00+00:00,Cost:8.00>]>
StageName:artist3 ,SocialLink: https://www.instagram.com/artist3/ <QuerySet [<Album: Name:hh,CreationDate:2022-10-07 09:01:19.665848+00:00,ReleaseDate:2205-01-01 00:00:00+00:00,Cost:8.00>]>
StageName:artist4 ,SocialLink: https://www.instagram.com/artist4/ <QuerySet [<Album: Name:hh,CreationDate:2022-10-07 09:00:33.362215+00:00,ReleaseDate:2205-01-01 00:00:00+00:00,Cost:8.00>]>
StageName:artist5 ,SocialLink: https://www.instagram.com/artist5/ <QuerySet [<Album: Name:help,CreationDate:2022-10-07 09:02:57.055218+00:00,ReleaseDate:2017-11-19 00:00:00+00:00,Cost:125.00>, <Album: Name:help,CreationDate:2022-10-07 09:03:09.210007+00:00,ReleaseDate:2017-11-19 00:00:00+00:00,Cost:125.00>]>
StageName:artist6 ,SocialLink: https://www.instagram.com/artist6/ <QuerySet []>
`
### second way
`for Alb in Album.objects.select_related('artist'):print(Alb.name,Alb.artist.Stage_name)`
 -----
`StageName:artist1 ,SocialLink: https://www.instagram.com/artist1/ <QuerySet [<Album: Name:Help i lost!,CreationDate:1997-10-19 00:00:00+00:00,ReleaseDate:1997-10-19 00:00:00+00:00,Cost:15.19>, <Album: Name:Help i lost!,CreationDate:2022-10-07 07:52:25.818482+00:00,ReleaseDate:1997-10-19 00:00:00+00:00,Cost:15.19>, <Album: Name:LOL!,CreationDate:2022-10-07 07:53:36.946724+00:00,ReleaseDate:2007-11-19 00:00:00+00:00,Cost:15.19>, <Album: Name:lol pro,CreationDate:2022-10-07 08:56:05.430014+00:00,ReleaseDate:2005-01-01 00:00:00+00:00,Cost:12.00>, <Album: Name:lol pro,CreationDate:2022-10-07 09:00:21.770458+00:00,ReleaseDate:2005-01-01 00:00:00+00:00,Cost:12.00>, <Album: Name:hh,CreationDate:2022-10-07 09:00:59.419060+00:00,ReleaseDate:2205-01-01 00:00:00+00:00,Cost:8.00>]>
StageName:artist2 ,SocialLink: https://www.instagram.com/artist2/ <QuerySet [<Album: Name:hh,CreationDate:2022-10-07 09:01:10.605074+00:00,ReleaseDate:2205-01-01 00:00:00+00:00,Cost:8.00>]>
StageName:artist3 ,SocialLink: https://www.instagram.com/artist3/ <QuerySet [<Album: Name:hh,CreationDate:2022-10-07 09:01:19.665848+00:00,ReleaseDate:2205-01-01 00:00:00+00:00,Cost:8.00>]>
StageName:artist4 ,SocialLink: https://www.instagram.com/artist4/ <QuerySet [<Album: Name:hh,CreationDate:2022-10-07 09:00:33.362215+00:00,ReleaseDate:2205-01-01 00:00:00+00:00,Cost:8.00>]>
StageName:artist5 ,SocialLink: https://www.instagram.com/artist5/ <QuerySet [<Album: Name:help,CreationDate:2022-10-07 09:02:57.055218+00:00,ReleaseDate:2017-11-19 00:00:00+00:00,Cost:125.00>, <Album: Name:help,CreationDate:2022-10-07 09:03:09.210007+00:00,ReleaseDate:2017-11-19 00:00:00+00:00,Cost:125.00>]>
StageName:artist6 ,SocialLink: https://www.instagram.com/artist6/ <QuerySet []>
`
## list down all albums ordered by cost then by name (cost has the higher priority)
`Album.objects.order_by('cost','name')`
-----
`<QuerySet [<Album: Name:hh,CreationDate:2022-10-07 09:00:33.362215+00:00,ReleaseDate:2205-01-01 00:00:00+00:00,Cost:8.00>, <Album: Name:hh,CreationDate:2022-10-07 09:00:59.419060+00:00,ReleaseDate:2205-01-01 00:00:00+00:00,Cost:8.00>, <Album: Name:hh,CreationDate:2022-10-07 09:01:10.605074+00:00,ReleaseDate:2205-01-01 00:00:00+00:00,Cost:8.00>, <Album: Name:hh,CreationDate:2022-10-07 09:01:19.665848+00:00,ReleaseDate:2205-01-01 00:00:00+00:00,Cost:8.00>, <Album: Name:lol pro,CreationDate:2022-10-07 08:56:05.430014+00:00,ReleaseDate:2005-01-01 00:00:00+00:00,Cost:12.00>, <Album: Name:lol pro,CreationDate:2022-10-07 09:00:21.770458+00:00,ReleaseDate:2005-01-01 00:00:00+00:00,Cost:12.00>, <Album: Name:Help i lost!,CreationDate:1997-10-19 00:00:00+00:00,ReleaseDate:1997-10-19 00:00:00+00:00,Cost:15.19>, <Album: Name:Help i lost!,CreationDate:2022-10-07 
07:52:25.818482+00:00,ReleaseDate:1997-10-19 00:00:00+00:00,Cost:15.19>, <Album: Name:LOL!,CreationDate:2022-10-07 07:53:36.946724+00:00,ReleaseDate:2007-11-19 00:00:00+00:00,Cost:15.19>, <Album: Name:help,CreationDate:2022-10-07 09:02:57.055218+00:00,ReleaseDate:2017-11-19 00:00:00+00:00,Cost:125.00>, <Album: Name:help,CreationDate:2022-10-07 09:03:09.210007+00:00,ReleaseDate:2017-11-19 00:00:00+00:00,Cost:125.00>]>`

##Modify the artist queryset so that I can order the list of art#sts by the number of their approved albums
`sorted(Artist.objects.all(),key=lambda t:t.approved_albums())`
---
`[<Artist: StageName:artist2 ,SocialLink: https://www.instagram.com/artist2/>,
 <Artist: StageName:artist3 ,SocialLink: https://www.instagram.com/artist3/>,
 <Artist: StageName:artist4 ,SocialLink: https://www.instagram.com/artist4/>,
 <Artist: StageName:artist5 ,SocialLink: https://www.instagram.com/artist5/>,
 <Artist: StageName:artist6 ,SocialLink: https://www.instagram.com/artist6/>,
 <Artist: StageName:artist1 ,SocialLink: https://www.instagram.com/artist1/>]`
