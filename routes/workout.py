from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, status , Body, Query
from fastapi import APIRouter, Depends, HTTPException
from models.models import User , Expert, Trainer
from models.schemas import Email, Login, RegistrationIn
from dependencies import get_user, JWT_SECRET

router = APIRouter()

async def load_cach():
    '''
    load the workout plans in a list as a cach memory
    '''
    pass

workout_plans = load_cach()


@router.get('/discover_workout')
async def discover_workout(user = Depends(get_user)):
    '''
    returns all workouts
    DB NOTE : you will create a model for the workout plans
    DB NOTE: each trainer has a list of the plans they do
    '''
    pass
    
@router.get('/workout')
async def workout(user = Depends(get_user)):
    '''
    returns basic info about the worksout plans based on the goals, and many other things
    costumised selection for each user
    '''
    pass


@router.get('/workout/{id}')
async def workout( id:int, user = Depends(get_user)):
    '''
    returns all info about the workout plan
    
    '''
    pass

