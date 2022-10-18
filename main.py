from datetime import datetime
from typing import List,Optional
from fastapi import FastAPI , HTTPException, Request
from odmantic import AIOEngine, Model,Field,ObjectId,Reference
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()
client=AsyncIOMotorClient('mongodb://localhost:27017')
engine = AIOEngine(client=client,database="testdb")

class UserFeed(Model):
    details:str
    challagenges:str
    status:str
    created_at:datetime=Field(index=True,default=datetime.today())
    updated_at:Optional[datetime]=Field(index=True,default=None)
class Users(Model):
    name: str
    username: str
    password: str
    role:str
    user_feed:List[UserFeed]
    created_at:datetime=Field(index=True,default=datetime.today())
    updated_at:Optional[datetime]=Field(index=True,default=None)
class Game(Model):
    game:str
    vanue:str
    players:List[Users]
    achivements:str
    created_at:datetime=Field(index=True,default=datetime.today())
    updated_at:Optional[datetime]=Field(index=True,default=None)
class Posts(Model):
    title:str
    content:str
    created_by:Users=Reference()
    likes:List[Users]
    dislikes:List[Users]
    created_at:datetime=Field(index=True,default=datetime.today())
    updated_at:Optional[datetime]=Field(index=True,default=None)
class Events(Model):
    vanue:str
    stars:List[Users]
    created_by:Users=Reference()
    likes:List[Users]
    dislikes:List[Users]
    created_at:datetime=Field(index=True,default=datetime.today())
    updated_at:Optional[datetime]=Field(index=True,default=None)

@app.get("/userslist/")
async def get_userslist():
    """_summary_
    Returns:
        _type_: _description_
    """
   
    users=await engine.find(Users,{})
    return users
@app.get("/getuser/{id}")
async def get_users(id:ObjectId):
    """_summary_
    Args:
        id (ObjectId): _description_
    Raises:
        HTTPException: _description_
    Returns:
        _type_: _description_
    """
    user = await engine.find_one(Users, Users.id == id)
    if user is None:
        raise HTTPException(404)
    return user
@app.put("/createusers/")
async def create_users(users: Users):
    """_summary_
    Args:
        users (Users): _description_
    Returns:
        _type_: _description_
    """
    await engine.save(users)
    return users
@app.get("/user/count", response_model=int)
async def count_users():
    """_summary_
    Returns:
        _type_: _description_
    """
    count = await engine.count(Users)
    return count
@app.get("/gamelist/")
async def get_gamelist():
    """_summary_
    Returns:
        _type_: _description_
    """
    games=await engine.find(Game)
    return games
@app.get("/getgames/{id}")
async def get_games(id:ObjectId):
    """_summary_
    Args:
        id (ObjectId): _description_
    Raises:
        HTTPException: _description_
    Returns:
        _type_: _description_
    """
    game = await engine.find_one(Game, Game.id == id)
    if game is None:
        raise HTTPException(404)
    return game
@app.put("/newgame/")
async def create_games(games: Game):
    """_summary_
    Args:
        users (Users): _description_
    Returns:
        _type_: _description_
    """
    await engine.save(games)
    return games
@app.get("/game/count")
async def count_games():
    """_summary_
    Returns:
        _type_: _description_
    """
    count = await engine.count(Game)
    return count
@app.get("/postlist/")
async def get_postlist():
    """_summary_
    Returns:
        _type_: _description_
    """
    posts=await engine.find(Posts)
    return posts
@app.get("/getposts/{id}")
async def get_posts(id:ObjectId):
    """_summary_
    Args:
        id (ObjectId): _description_
    Raises:
        HTTPException: _description_
    Returns:
        _type_: _description_
    """
    posts = await engine.find_one(Posts, Posts.id == id)
    if posts is None:
        raise HTTPException(404)
    return posts
@app.put("/newpost/")
async def create_post(posts: Posts):
    """_summary_
    Args:
        users (Users): _description_
    Returns:
        _type_: _description_
    """
    await engine.save(posts)
    return posts
@app.get("/post/count")
async def count_post():
    """_summary_
    Returns:
        _type_: _description_
    """
    count = await engine.count(Posts)
    return count
@app.get("/eventlist/")
async def get_eventlist():
    """_summary_
    Returns:
        _type_: _description_
    """
    events=await engine.find(Events)
    return events
@app.get("/getevents/{id}")
async def get_events(id:ObjectId):
    """_summary_
    Args:
        id (ObjectId): _description_
    Raises:
        HTTPException: _description_
    Returns:
        _type_: _description_
    """
    events = await engine.find_one(Events, Events.id == id)
    if events is None:
        raise HTTPException(404)
    return events
@app.put("/newevents/")
async def create_events(events: Events):
    """_summary_
    Args:
        users (Users): _description_
    Returns:
        _type_: _description_
    """
    await engine.save(events)
    return events
@app.get("/events/count")
async def count_events():
    """_summary_
    Returns:
        _type_: _description_
    """
    count = await engine.count(Events)
    return count
@app.get("/userfeedlist/")
async def get_userfeedlist():
    """_summary_
    Returns:
        _type_: _description_
    """
    userfeed=await engine.find(UserFeed)
    return userfeed
@app.get("/getuserfeed/{id}")
async def get_userfeed(id:ObjectId):
    """_summary_
    Args:
        id (ObjectId): _description_
    Raises:
        HTTPException: _description_
    Returns:
        _type_: _description_
    """
    userfeed = await engine.find_one(UserFeed, UserFeed.id == id)
    if userfeed is None:
        raise HTTPException(404)
    return userfeed
@app.put("/newuserfeed/")
async def create_userfeed(userfeed: UserFeed):
    """_summary_
    Args:
        users (Users): _description_
    Returns:
        _type_: _description_
    """
    await engine.save(userfeed)
    return userfeed
@app.get("/userfeed/count")
async def count_userfeed():
    """_summary_
    Returns:
        _type_: _description_
    """
    count = await engine.count(UserFeed)
    return count
@app.get("/userwisedata/")
async def userwisedata(request: Request):
    """_summary_
    Returns:
        _type_: _description_
    """
    parms=request.query_params
    print(parms,type(parms))
    count = await engine.find(Users,parms)
    return count
@app.get("/userwisedata/")
async def userwisedataget(request: Request):
    """_summary_
    Returns:
        _type_: _description_
    """
    parms=request.query_params
    print(parms,type(parms))
    count = await engine.find(Users,parms)
    return count
@app.get("/Gamewisedata/")
async def Gamewisedata(request: Request):
    """_summary_
    Returns:
        _type_: _description_
    """
    parms=request.query_params
    print(parms,type(parms))
    count = await engine.find(Game,parms)
    return count
@app.get("/Gamewisedata/")
async def gamewisedata(request: Request):
    """_summary_
    Returns:
        _type_: _description_
    """
    parms=request.query_params
    print(parms,type(parms))
    count = await engine.find(Game,parms)
    return count
@app.get("/postwisedata/")
async def postwisedata(request: Request):
    """_summary_
    Returns:
        _type_: _description_
    """
    parms=request.query_params
    print(parms,type(parms))
    count = await engine.find(Posts,parms)
    return count
@app.get("/eventwisedata/")
async def eventwisedata(request: Request):
    """_summary_
    Returns:
        _type_: _description_
    """
    parms=request.query_params
    print(parms)
    count = await engine.find(Events,parms)
    return count
