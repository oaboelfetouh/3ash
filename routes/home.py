from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, status , Body, Query
from fastapi import APIRouter, Depends, HTTPException
from models.models import User , Expert, Trainer
from models.schemas import Email, Login, RegistrationIn

router = APIRouter()
