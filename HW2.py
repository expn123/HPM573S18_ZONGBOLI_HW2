# Health Utilities Index Mark3 (HUI3)
Constant1 = 1.371
Constant2 = 0.371
dictCoefficients = {'Vision':       [1,0.98,0.89,0.84,0.75,0.61],
                    'Hearing':      [1,0.95,0.89,0.80,0.74,0.61],
                    'Speech':       [1,0.94,0.89,0.81,0.68],
                    'Ambulation':   [1,0.93,0.86,0.73,0.65,0.58],
                    'Dexterity':    [1,0.95,0.88,0.76,0.65,0.56],
                    'Emotion':      [1,0.95,0.85,0.64,0.46],
                    'Cognition':    [1,0.92,0.95,0.83,0.60,0.42],
                    'Pain':         [1,0.96,0.90,0.77,0.55]
                    };

def get_score(vision,hearing,speech,ambulation,dexterity,emotion,cognition,pain):
    """

    :param vision: level of vision
    :param hearing:level of hearing
    :param speech:level of speech
    :param ambulation:level of ambulation
    :param dexterity:level of dexterity
    :param emotion:level of emotion
    :param cognition:level of cognition
    :param pain:level of pain
    :return: final score of HUI3
    """
    # ensure the range of score
    if not(vision in [1,2,3,4,5,6]):
        raise ValueError("Vision level can only take 1~6(integer)")
    if not(hearing in [1,2,3,4,5,6]):
        raise ValueError("Hearing level can only take 1~6(integer)")
    if not(speech in [1,2,3,4,5]):
        raise ValueError("Speech level can only take 1~6(integer)")
    if not(ambulation in [1,2,3,4,5,6]):
        raise ValueError("Ambulation level can only take 1~6(integer)")
    if not(dexterity in [1,2,3,4,5,6]):
        raise ValueError("Dexterity level can only take 1~6(integer)")
    if not(emotion in [1,2,3,4,5,6]):
        raise ValueError("Emotion level can only take 1~6(integer)")
    if not(cognition in [1,2,3,4,5,6]):
        raise ValueError("Cognition level can only take 1~6(integer)")
    if not(pain in [1,2,3,4,5]):
        raise ValueError("Pain level can only take 1~6(integer)")


    #get b1-b8
    b1=dictCoefficients['Vision'][vision-1]
    b2=dictCoefficients['Hearing'][hearing-1]
    b3=dictCoefficients['Speech'][speech-1]
    b4=dictCoefficients['Ambulation'][ambulation-1]
    b5=dictCoefficients['Dexterity'][dexterity-1]
    b6=dictCoefficients['Emotion'][emotion-1]
    b7=dictCoefficients['Cognition'][cognition-1]
    b8=dictCoefficients['Pain'][pain-1]

    # get the final score
    score= Constant1*(b1*b2*b3*b4*b5*b6*b7*b8)-Constant2

    return score

