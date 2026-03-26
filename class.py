class RubicCube:
    def __init__(self):
        for i in range(1 ,10):
            print("Enter all the side on the white colour")
            for i in range(1,10):
                (input(f"Enter the {i} peice colour: "))
                
    side = {
        "side1" : ['W','W','W','W','W','W','W','W','W'] ,
        "side2" : ['Y','Y','Y','Y','Y','Y','Y','Y','Y'] ,
        "side3" : ['R','R','R','R','R','R','R','R','R'] ,
        "side4" : ['G','G','G','G','G','G','G','G','G'] ,
        "side5" : ['O','O','O','O','O','O','O','O','O'] ,
        "side6" : ['B','B','B','B','B','B','B','B','B'] 
    }

