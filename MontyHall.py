import random as r
import pandas as pd

def monty_hall(no_of_sim,change_door=False):
    wins=0
    losses=0
    list_of_doors=[1,2,3]

    chosen_doors=[]
    car_doors=[]
    revealed_doors=[]
    new_chosen_doors=[]
    win_or_loss=[]
    games=[i for i in range(1,no_of_sim+1)]

    for _ in range(no_of_sim):

        chosen_door=r.choice(list_of_doors)
        car_door=r.choice(list_of_doors)
        revealed_door=r.choice([x for x in list_of_doors if x!=car_door and x!=chosen_door])

        if change_door:

            new_chosen_door=r.choice([x for x in list_of_doors if x!=chosen_door and x!=revealed_door])

            if new_chosen_door==car_door:
                wins+=1
                win_or_loss.append('Win')
            else:
                losses+=1
                win_or_loss.append('Loss')

            chosen_doors.append(chosen_door)
            car_doors.append(car_door)
            revealed_doors.append(revealed_door)
            new_chosen_doors.append(new_chosen_door)
        
        else:

            if chosen_door==car_door:
                wins+=1
                win_or_loss.append('Win')
            else:
                losses+=1
                win_or_loss.append('Loss')
            
            
            chosen_doors.append(chosen_door)
            car_doors.append(car_door)
            revealed_doors.append(revealed_door)
            new_chosen_doors.append(None)

    df=pd.DataFrame({'Game no.':games,
                     'Chosen Door':chosen_doors,
                     'Car Door': car_doors,
                     'Revealed Door': revealed_doors,
                     'New chosen door':new_chosen_doors,
                     'Win/Loss':win_or_loss})
    
    df.set_index('Game no.',inplace=True)

    win_probability=wins/no_of_sim
    loss_probabilty=1-win_probability

    print(f'Number of Games: {no_of_sim}')
    print(f'Win Probabilty: {win_probability}')
    print(f'Loss Probabilty: {loss_probabilty}')

    return df

monty_hall(no_of_sim=1000,change_door=True)




