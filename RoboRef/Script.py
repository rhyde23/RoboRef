#Starting Code

"""
General Scheme

While True :
always do updateCurrentRedirection(new_ball_position)
if in updateCurrentRedirection(new_ball_position), we find a redirection,
    1st: Find positions of every player on field*
    2nd: find player index of player who redirected using current_positions by first finding the basic candidates
    3rd: See if offsides 
    4th: If not offsides, just update current_redirection and retrospective_offsides
if not :
    update values in current_redirection
"""




#Emphasis on indexes
#Only record retrospective offsides



#NOTE: Also could possibly include a list to keep track of player compass directions to assist the "getRedirectIdentity" function, but this does not include that yet
#NOTE: Order of indexes will likely be 0-10 = team 1, 11-21 = team 2
#NOTE: Might want to find more efficient way to find identity of redirect because right now its getting every single player coord and thats the only time it ever needs to do that


#Function to retrieve data from the GPS trackers
#type and rtype unknown
def updateGPSPositions() :
    pass



#Function to retrieve data from the ball's GPS
#type and rtype unknown
def updateBallPosition() :
    pass



#Function to update global list "retrospective_offsides", which records the indexes of players of offsides players at the time of a redirect
#NOTE: ONLY TO BE USED AT TIME OF REDIRECT
#type: list "current_positions" will contain all of the current player positions in order
#type: int current_redirection[x] or separate int input ---> basically we need to have the INDEX of who just redirected (look for same team, offsides, and NOT THIS NUMBER)
#rtype: will update global list "retrospective_offsides"
def updateRetrospectiveOffsides(current_positions) :
    pass



#This list will contain all the relevant info about the ball's most recent redirection
#index of player who redirected, velocity, acceleration
#Could also represent velocity and acceleration as x_change_per_update and y_change_per_update
current_redirection = []



#This list will contain all of the indexes of the players who were offsides at the time of last redirect
#The purpose of this list is to check if a new redirection detected in "updateCurrentRedirection" was made by a player in this list. If so, offsides
retrospective_offsides = []



#type: current_positions: list of all current player coords at the time of recent redirect we're trying to identify
#type: ball_position: coordinate of ball position
#rtype: list candidates_positions and list candidates_directions and list candidates_indexes
#ORRRR: {} key = index, value = [position, direction]
#NOTE: IF THERE IS A WAY TO POSSIBLY DETECT THE GPS's CLOSEST TO THE BALL GPS, THAT WOULD ALLOW US TO BYPASS THIS FUNCTION AND POSSIBLY SAVE RUNTIME
#NOTE: Constant needs to be decided: How far away from ball does a player have to be to be considered a candidate

min_distance_from_ball = None

def getCandidatesOfRedirect(current_positions, ball_position) :
    pass



#Function that will use gps positions and ball position to find who just redirected the ball in the case of redirect detection "updateCurrentRedirection"
#type: candidates_positions: list of player coordinates that COULD have redirected ball
#type: candidates_directions: list of player directions that COULD have redirected ball
#type: ball_position: coordinate of ball position
#rtype: integer representing the player's index who redirected ball
#NOTE: These three lists can also be in the form of one dictionary
#NOTE: This function will indirectly call offsides because if its return value is in retrospective_offsides (before it gets updated), then we call offsides
def getRedirectIdentity(candidates_positions, candidates_directions, candidates_indexes, ball_position) :
    pass



#Function that takes in the new_ball_position and updates the current_redirection list and the retrospective_offsides list by either just updating the velocity and acceleration or detecting a new redirect and adjusting.
#This function will edit the global lists "current_redirection" and "retrospective_offsides", so it should only return a boolean value to represent offsides or not
#type: new_ball_position coordinate will tell us where the ball currently is
#type: current_redirection ----- we will use this to detect a new redirection
#rtype: boolean to represent if offsides, AND ALSO WILL EDIT GLOBAL retrospective_offsides and current_redirection if False
def updateCurrentRedirection(new_ball_position) :
    pass



while True :
    gps_positions = getGPSPositions()
    ball_position = getBallPosition()
    updateCurrentRedirection(ball_position)
    
    

