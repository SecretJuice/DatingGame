import pygame
import pygame_gui
import random

WINDOW_SIZE = (480*2, 270*2)

def SomeFunc(*params):
    print("ima null func")


def SomeOtherFunc(*params):
    print("yet another func")
    ChangeEmotion(random.randint(1,3))

def TraitsCheck(option):

    """Returns list of how many positive and negative traits match"""

    matches = [[], []]

    positive = current_scenario[option]['positive_traits']
    negative = current_scenario[option]["negative_traits"]

    for trait in current_traits:
        if trait in positive:
            matches[0].append(trait)
        if trait in negative:
            matches[1].append(trait)
    
    print(matches)
    return matches

def EvaluateOption(option):

    pos, neg = TraitsCheck(option)

    if len(pos) > len(neg):
        EditScore(1)
        ChangeEmotion(2)
    elif len(pos) < len(neg):
        EditScore(-1)
        AddStrike(neg)
        ChangeEmotion(0)
    elif len(pos) == len(neg):
        ChangeEmotion(1)

    SelectScenario()

def StatCheck(option, stat):

    stat_value = current_player_stats[stat]
    pos, neg = TraitsCheck(option)

    if random.randint(1, 4) <= stat_value:
        EditScore(2)
        ChangeEmotion(3)
        print("Passed the stat roll")
    else:
        EditScore(-2)
        AddStrike(neg)
        ChangeEmotion(0)
        print("Failed stat roll")
    
    SelectScenario()
    #Feedback, tell player result and why

def CheckScenarioValidity():
    
    """Returns True or False depending on whether this particular scenario should be shown to the player in this run"""

    option_a = TraitsCheck("option_a")
    option_b = TraitsCheck("option_b")

    if len(option_a[0]) > len(option_a[1]) and len(option_b[0]) > len(option_b[1]):
        return False
    if len(option_a[0]) < len(option_a[1]) and len(option_b[0]) < len(option_b[1]):
        return False
    if len(option_a[0]) == len(option_a[1]) and len(option_b[0]) == len(option_b[1]):
        return False
    if len(option_a[0]) == 0 and len(option_a[1]) == 0 and len(option_b[0]) == 0 and len(option_b[1]) == 0:
        return False
    
    return True

def SelectScenario():

    valid = False

    while not valid:
        LoadScenario(random.randint(0, len(scenarios) - 1))
        valid = CheckScenarioValidity()

current_scenario = None

scenarios = [
            {'scenario': "Basically this thing happened what are you going to do about it you scared i bet your scared you scaredy cat",
            'option_a': {

                "text": "Option text that shows up in box",
                "positive_traits": ["affectionate", "jealous", "attentive", "possessive", "caring", "moody", "devoted", "stubborn"],
                "negative_traits": ["insecure", "romantic", "needy", "considerate", "temperamental", "trustworthy", "empathetic"],
                "display_function": SomeFunc,
                "activation_function": EvaluateOption,
                "display_func_params": [],
                "activation_func_params": ["option_a"]

            },
            'option_b': {

                "text": "This is a stat check",
                "positive_traits": ["judgmental", "communicative", "distrustful", "compassionate", "manipulative", "dedicated"],
                "negative_traits": ["supportive", "clingy", "understanding", "distant", "adventurous", "impulsive", "open-minded", "critical", "spontaneous"],
                "display_function": SomeFunc,
                "activation_function": StatCheck,
                "display_func_params": [],
                "activation_func_params": ['option_b', "suave"]
            }},
            {
            'scenario': "Your partner wants to spend the day with you, but you had already made plans with your friends. What do you do?",
            'option_a': {
                "text": "Cancel plans with your friends and spend the day with your partner",
                "positive_traits": ["affectionate", "attentive", "caring"],
                "negative_traits": ["independent", "spontaneous", "open-minded"],
                "display_function": SomeFunc,
                "activation_function": EvaluateOption,
                "display_func_params": [],
                "activation_func_params": ["option_a"]
            },
            'option_b': {
                "text": "Explain the situation to your partner and stick with your original plans",
                "positive_traits": ["independent", "spontaneous", "open-minded"],
                "negative_traits": ["affectionate", "attentive", "caring"],
                "display_function": SomeFunc,
                "activation_function": EvaluateOption,
                "display_func_params": [],
                "activation_func_params": ['option_b']
            }
            },

            {
            'scenario': "You and your partner are planning a trip, but they want to go somewhere you have already been. What do you do?",
            'option_a': {
                "text": "Agree to go to the place your partner wants to go to",
                "positive_traits": ["flexible", "adventurous", "considerate"],
                "negative_traits": ["stubborn", "judgmental", "demanding"],
                "display_function": SomeFunc,
                "activation_function": EvaluateOption,
                "display_func_params": [],
                "activation_func_params": ["option_a"]
            },
            'option_b': {
                "text": "Suggest an alternative destination that you both have not been to before",
                "positive_traits": ["considerate", "adventurous", "flexible"],
                "negative_traits": ["stubborn", "judgmental", "demanding"],
                "display_function": SomeFunc,
                "activation_function": EvaluateOption,
                "display_func_params": [],
                "activation_func_params": ['option_b']
            }
            },

            {
            'scenario': "Your partner has been having a difficult time at work and comes home stressed every day. How do you help them relax?",
            'option_a': {
                "text": "Cook them a nice meal and give them a massage",
                "positive_traits": ["compassionate", "understanding", "affectionate"],
                "negative_traits": ["manipulative", "clingy", "needy"],
                "display_function": SomeFunc,
                "activation_function": EvaluateOption,
                "display_func_params": [],
                "activation_func_params": ["option_a"]
            },
            'option_b': {
                "text": "Give them some space to unwind and offer to listen if they want to talk",
                "positive_traits": ["independent", "understanding", "supportive"],
                "negative_traits": ["needy", "clingy", "manipulative"],
                "display_function": SomeFunc,
                "activation_function": EvaluateOption,
                "display_func_params": [],
                "activation_func_params": ['option_b']
            }
            },
            {'scenario': "Your significant other is feeling overwhelmed at work and needs to cancel your date night. What do you do?",
            'option_a': {

            "text": "Get angry and take it personally",
            "positive_traits": ["possessive", "demanding"],
            "negative_traits": ["empathetic", "supportive"],
            "display_function": SomeFunc,
            "activation_function": EvaluateOption,
            "display_func_params": [],
            "activation_func_params": ["option_a"]
            },
            'option_b': {

            "text": "Show empathy and offer to help them in any way you can",
            "positive_traits": ["empathetic", "supportive", "understanding"],
            "negative_traits": ["judgmental", "distrustful"],
            "display_function": SomeFunc,
            "activation_function": EvaluateOption,
            "display_func_params": [],
            "activation_func_params": ['option_b']
            }},

            {'scenario': "Your significant other surprises you with a gift that you don't like. What do you do?",
            'option_a': {

            "text": "Pretend to like it and keep it anyway",
            "positive_traits": ["considerate", "affectionate"],
            "negative_traits": ["honest", "critical"],
            "display_function": SomeFunc,
            "activation_function": EvaluateOption,
            "display_func_params": [],
            "activation_func_params": ["option_a"]
            },
            'option_b': {

            "text": "Express your appreciation but kindly ask if it's possible to exchange it for something else",
            "positive_traits": ["honest", "considerate", "communicative"],
            "negative_traits": ["demanding", "manipulative"],
            "display_function": SomeFunc,
            "activation_function": EvaluateOption,
            "display_func_params": [],
            "activation_func_params": ['option_b']
            }},

            {'scenario': "Your significant other has been hanging out with a friend you don't particularly like. What do you do?",
            'option_a': {

            "text": "Demand that they stop spending time with that friend",
            "positive_traits": ["jealous", "possessive"],
            "negative_traits": ["open-minded", "compassionate"],
            "display_function": SomeFunc,
            "activation_function": EvaluateOption,
            "display_func_params": [],
            "activation_func_params": ["option_a"]
            },
            'option_b': {

            "text": "Express your concerns about the friend but trust your significant other's judgment",
            "positive_traits": ["communicative", "trustworthy"],
            "negative_traits": ["distrustful", "judgmental"],
            "display_function": SomeFunc,
            "activation_function": EvaluateOption,
            "display_func_params": [],
            "activation_func_params": ['option_b']
            }}
            ]

              # Need Scenario text, traits that favor, traits that dont, stat features

pygame.init()

pygame.mixer.init()

def LoadImage(image_name, scale=2):
    image = pygame.image.load(f"resources/images/{image_name}")
    print(f"Loaded {image_name}")
    return pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))

def LoadMusic(file_name):

    pygame.mixer.music.load(f"resources/sounds/music/{file_name}")
    pygame.mixer.music.play(-1)


pygame.display.set_caption('Dating Game')
window_surface = pygame.display.set_mode(WINDOW_SIZE)

def PlaceCentered(element, pos, surface=window_surface):
    surface.blit(element, (pos[0] - (element.get_width() / 2), pos[1] - (element.get_height() / 2)))

def WriteOutText(text, font, color, timestep=0):
    '''This is meant to write out text sequentially, for now just make the text'''

    return font.render(text, False, color)

def RenderElement(element, pos, surface=window_surface):
    surface.blit(element, pos)

def PlaceMultiline(text, font, color, pos, max_width, centered=False):
    lines = []

    sentence = ""
    for word in text.split():
        line_width = font.render(sentence + word, False, color).get_width()
        if line_width > max_width:
            lines.append(sentence)
            sentence = ""
        sentence += word + " "
    if sentence != "":
        lines.append(sentence)
    
    for line in range(len(lines)):

        line_element = font.render(lines[line], False, color)

        line_pos = (pos[0], pos[1] + ((line_element.get_height() * line) + 8))

        if centered:
            PlaceCentered(line_element, line_pos)
        else:
            RenderElement(line_element, line_pos)

def tint(surf, tint_color):
    """ adds tint_color onto surf.
    """
    surf = surf.copy()
    surf.fill(tint_color, None, pygame.BLEND_RGBA_MULT)
    return surf

date_names = {

    "male": ["Liam", "Noah", "Oliver", "William", "Elijah", "James", "Benjamin", "Lucas", "Mason", "Ethan", "Alexander", "Henry", "Jacob", "Michael", "Daniel", "Logan", "Jackson", "Sebastian", "Aiden", "Matthew", "Samuel", "David", "Joseph", "Carter", "Owen", "Wyatt", "John", "Jack", "Luke", "Jayden"],
    "female": ["Sophia", "Emma", "Olivia", "Ava", "Isabella", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn", "Abigail", "Emily", "Ella", "Elizabeth", "Camila", "Luna", "Sofia", "Avery", "Mila", "Aria", "Scarlett", "Penelope", "Layla", "Chloe", "Victoria", "Madison", "Eleanor", "Grace", "Nora", "Riley"]

} 

traits = ["affectionate", "jealous", "attentive", "possessive", "caring", "moody", "devoted", "stubborn", "empathetic", "insecure", "romantic", "needy", "considerate", "temperamental", "trustworthy", "judgmental", "communicative", "distrustful", "compassionate", "manipulative", "dedicated", "demanding", "supportive", "clingy", "understanding", "distant", "adventurous", "impulsive", "open-minded", "critical", "spontaneous"]




date_portrait_images = {

    "male": {

        "base": [ LoadImage("dateportrait/base_male_1.png") ],
        "clothing": [ LoadImage(f"dateportrait/clothing_male_{i+1}.png") for i in range(4) ],
        "accessories": [ LoadImage('dateportrait/glasses_male_1.png'), None],
        "facial_hair": [ LoadImage(f"dateportrait/facialhair_male_{i+1}.png") for i in range(5) ],
        "hair": [ LoadImage(f"dateportrait/hair_male_{i+1}.png") for i in range(8) ]

    },
    "female": {

        "base": [ LoadImage("dateportrait/base_female.png") ],
        "clothing": [ LoadImage(f"dateportrait/clothing_female_{i+1}.png") for i in range(6) ],
        "accessories": [ LoadImage('dateportrait/glasses_female_1.png'), None],
        "hair": [ LoadImage(f"dateportrait/hair_female_{i+1}.png") for i in range(11) ]

    }

}

date_portrait_colors = {

    "base": [pygame.color.Color("#f7d3c0"), pygame.color.Color("#815a4a"), pygame.color.Color("#f9c6a7")],
    "clothing": [pygame.color.Color("#66243e"), pygame.color.Color("#667c5e"), pygame.color.Color("#34172f"), pygame.color.Color("#c8b372")],
    "accessories": [pygame.color.Color("#66243e"), pygame.color.Color("#667c5e")],
    "hair": [pygame.color.Color("#66243e"), pygame.color.Color("#9a603f"), pygame.color.Color("#34172f"), pygame.color.Color("#f1bc8b")],
    "facial_hair": [pygame.color.Color("#66243e"), pygame.color.Color("#9a603f"), pygame.color.Color("#34172f"), pygame.color.Color("#f1bc8b")]

}


def BuildDatePortrait(gender):

    portrait_options = date_portrait_images[gender]

    date_portrait = {

    "base": None,
    "clothing": None,
    "accessories": None,
    "hair": None

    }

    if gender == "male":
        date_portrait["facial_hair"] = None

    for category in portrait_options:

        choice = random.choice(portrait_options[category])

        if choice != None:

            choice = tint(choice, random.choice(date_portrait_colors[category]))

            date_portrait[category] = choice
    
    return date_portrait

def DisplayDatePortrait(portrait):

    pos = (70, 12)

    for category in portrait:

        if portrait[category] != None:
            RenderElement(portrait[category], pos)

current_date_portrait = BuildDatePortrait("female")

background = LoadImage("gui/background.png")
title_screen = LoadImage("gui/title_screen.png")
text_card = LoadImage("gui/text_card.png")
selection_screen = LoadImage("gui/selection_screen.png")

empathy_icon = LoadImage("icons/empathy.png")
quickthinking_icon = LoadImage("icons/quickthinking.png")
suave_icon = LoadImage("icons/suave.png")

heart_whole_icon = LoadImage('icons/heart_whole.png')
heart_broken_icon = LoadImage('icons/heart_broken.png')

emotion_icons = [LoadImage(f"icons/emoji_{i+1}.png") for i in range(4)]

show_emotion = True
current_emotion = emotion_icons[0]

clock_subs = {

    "emotion_icon": 0,
    "black_fade": 0

}

function_schedule = {}

def SchedualFunction(secs, func, params=[]):

    global clock_subs
    global function_schedule

    if func in function_schedule:
        print(func)
        return

    function_schedule[func] = params
    clock_subs[func] = secs

def CheckFuncSchedual():

    global clock_subs
    global function_schedule

    execute_funcs = []

    for func in function_schedule:

        if GetClockValue(func) <= 0:

            execute_funcs.append(func)

    for func in execute_funcs:

        clock_subs.pop(func)
        ExecuteSchedualedFunc(func, function_schedule.pop(func))

def ExecuteSchedualedFunc(func, params):
    print(f"Executing {func} with {params}")
    func(*params)

def GetClockValue(clock):
    return clock_subs[clock]

def SetClockValue(clock, value):
    global clock_subs
    clock_subs[clock] = value

def ChangeEmotion(emote_level):

    global current_emotion
    current_emotion = emotion_icons[emote_level]

    clock_subs['emotion_icon'] = 1

def ShowEmotion():

    if GetClockValue("emotion_icon") > 0:
        RenderElement(current_emotion, (310, 50))

def ShowStrikes(strikes):

    pos = (80, 40)

    image = heart_broken_icon

    for i in range(2):
        if strikes <= 0:
            image = heart_whole_icon
        
        RenderElement(image, (pos[0] + (55 * i), pos[1]))
        strikes -= 1

def UpdateClockSubscribers(delta):
    
    for clock in clock_subs:


        clock_subs[clock] -= delta

        if clock_subs[clock] <= 0:
            clock_subs[clock] = 0
        
        # print(clock, clock_subs[clock])

fade_to_black = False
fade_rate = 2

def FadeToFromBlack():

    multiplier = 0

    if fade_to_black == False:
        multiplier = GetClockValue("black_fade") / fade_rate
    else:
        multiplier = 1 - (GetClockValue("black_fade") / fade_rate)

    surface = pygame.Surface(WINDOW_SIZE)
    surface.set_alpha(multiplier * 255)
    surface.fill((0,0,0))
    RenderElement(surface, (0,0))

def FadeToBlack(rate):
    global fade_to_black
    global fade_rate

    fade_rate = rate
    fade_to_black = True
    ChangeUIClickable(False)
    

    SetClockValue("black_fade", rate)

def FadeFromBlack(rate):
    global fade_to_black
    global fade_rate

    fade_rate = rate
    fade_to_black = False
    SchedualFunction(rate, ChangeUIClickable, [True])
    SetClockValue("black_fade", rate)

manager = pygame_gui.UIManager(WINDOW_SIZE, "resources/theme.json")

body_font = pygame.font.Font("resources/Greenscr.ttf", 12)
header_font = pygame.font.Font("resources/Greenscr.ttf", 20)

def LoadUI(elements):

    for element in ui_elements:
        if element in elements:
            element.show()
        else:
            element.hide()

option_a_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((387, 215), (242, 245)),
                                            text="",
                                            manager=manager)

option_b_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((640, 215), (242, 245)),
                                            text="",
                                            manager=manager)

play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((535, 369), (172, 64)),
                                           text="",
                                           manager=manager )

male_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((228, 307), (172, 64)),
                                           text="",
                                           manager=manager )

female_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((560, 307), (172, 64)),
                                           text="",
                                           manager=manager )

ui_elements =[option_a_button, option_b_button, play_button, male_button, female_button]

gender_preference = "female"

partner_traits_header = header_font.render("Traits", False, (255, 255, 255))

partner_name_text = "Gertrude's sister"

scenario_text = "Hey this thing happened"

option_a_text = "Yep he do be doin the do tho but what if i put a bunch of text here would it be too much to handle???"
option_b_text = "Oh boi there he go again"

current_player_stats = {'suave': 1, 'empathy': 1, 'quick-thinking': 1}
current_strikes = 0

current_traits = ["Quiet", "Smart", "Clean-freak", "Observant", "Scary", "Smooth"]

learned_traits = []

traits_texts = []



current_score = 0

def SetupRun():
    CreateSO(gender_preference)

    global current_strikes
    global current_score
    current_strikes = 0
    current_score = 0

    print(learned_traits)
    LoadScenario(0)

def RestartGame(learned_trait):
    FadeToBlack(1)
    SchedualFunction(1, ChangeScene, [DisplayTextCard, [f"Your SO died. It's your fault. Feel bad.\nbtw your learned the '{learned_trait.capitalize()}' trait"], OnLoadTextCard])


def CheckFailState(traits):

    global learned_traits

    if current_strikes >= 2:
        print("The game is lost")

        learned = LearnTrait(traits)

        RestartGame(learned)

def LearnTrait(traits):
    for trait in traits:
        if not trait in learned_traits:
            learned_traits.append(trait)
            return trait

def WinGame(name):
    FadeToBlack(1)
    SchedualFunction(1, ChangeScene, [DisplayTextCard, [f"you might not know everything about partner, but that okay! You will dicover more and you love eac other. If you love eac other enough, you get through everythig!"], OnLoadWinTextCard])

def CheckWinState():
    if current_score >= 5:
        print("The Game is won!")
        WinGame(partner_name_text)

def EditScore(increment):
    global current_score
    current_score += increment

    if current_score <= 0: current_score = 0 

    print(f"Current Score {current_score}")
    CheckWinState()

def AddStrike(traits):
    global current_strikes
    current_strikes += 1
    CheckFailState(traits)





def CreateSO(gender):
    global partner_name_text
    global current_traits
    global current_date_portrait

    partner_name_text = random.choice(date_names[gender])

    local_traits = []

    while len(local_traits) < 6:
        pick = random.choice(traits)

        if not pick in local_traits: 
            local_traits.append(pick)
    
    current_traits = local_traits

    global traits_texts
    traits_texts = []

    for trait in current_traits:
        if trait in learned_traits:
            traits_texts.append(body_font.render(trait.capitalize(), False, (255, 255, 255)))
        else:
            traits_texts.append(body_font.render("-----", False, (255, 255, 255)))

    current_date_portrait = BuildDatePortrait(gender)
        

option_a_function = SomeFunc
option_a_func_params = []
option_b_function = SomeOtherFunc
option_b_func_params = []



def LoadScenario(index):

    global current_scenario
    global scenario_text
    global option_a_text
    global option_b_text
    global option_a_function
    global option_a_func_params
    global option_b_function
    global option_b_func_params

    current_scenario = scenarios[index]

    scenario_text = current_scenario['scenario']
    option_a_text = current_scenario['option_a']['text']
    option_b_text = current_scenario['option_b']['text']

    option_a_function = current_scenario['option_a']['activation_function']
    option_a_func_params = current_scenario['option_a']['activation_func_params']

    option_b_function = current_scenario['option_b']['activation_function']
    option_b_func_params = current_scenario['option_b']['activation_func_params']


SetupRun()



def OptionA():
    option_a_function(*option_a_func_params)


def OptionB():
    option_b_function(*option_b_func_params)

def PlayButton():
    FadeToBlack(1)
    SchedualFunction(1, ChangeScene, [DisplayGenderSelect, [], SomeFunc])

def MaleButton():
    global gender_preference
    gender_preference = "male"
    FadeToBlack(1)
    SchedualFunction(1, ChangeScene, [DisplayTextCard, ["It takes a lot of time to get to know someone, and sometimes you need some practices to be a good partner. Let's play Kiss and Breakup!"], OnLoadTextCard])

def FemaleButton():
    global gender_preference
    gender_preference = "female"
    FadeToBlack(1)
    SchedualFunction(1, ChangeScene, [DisplayTextCard, ["It takes a lot of time to get to know someone, and sometimes you need some practices to be a good partner. Let's play Kiss and Breakup!"], OnLoadTextCard])

ui_clickable = False

def ChangeUIClickable(clickable):

    global ui_clickable
    ui_clickable = clickable

def ProcessButtonClickFunctions(ui_button):

    if ui_clickable == False: return

    button_functions = {option_a_button: OptionA,
                        option_b_button: OptionB,
                        play_button: PlayButton,
                        male_button: MaleButton,
                        female_button: FemaleButton}
    button_functions[ui_button]()

FadeFromBlack(1)

clock = pygame.time.Clock()

# def AnimationController():

is_running = True



def DisplayMainGame():

    LoadUI([option_a_button, option_b_button])
    RenderElement(background, (0, 0))
    
    DisplayDatePortrait(current_date_portrait)

    PlaceCentered(WriteOutText(partner_name_text, header_font, (255, 255, 200)), (230, 391))
    RenderElement(partner_traits_header, (188, 420))
    PlaceMultiline(scenario_text, header_font, (20, 20, 20), (410, 50), 400)
    PlaceMultiline(option_a_text, header_font, (20, 20, 20), (512, 236), 200, True)
    PlaceMultiline(option_b_text, header_font, (20, 20, 20), (762, 236), 200, True)
    RenderElement(suave_icon, (390, 464))
    RenderElement(empathy_icon, (560, 464))
    RenderElement(quickthinking_icon, (730, 464))
    ShowEmotion()
    ShowStrikes(current_strikes)
  

    for index in range(len(traits_texts)):
        if index < 3:
            RenderElement(traits_texts[index], (110, 456 + (index * 22)))
        else:
            RenderElement(traits_texts[index], (240, 456 + ((index - 3) * 22)))

    if ui_clickable: manager.draw_ui(window_surface)

def DisplayTitleScreen():

    LoadUI([play_button])

    RenderElement(title_screen, (0, 0))
    RenderElement(header_font.render("Play", False, (255, 255, 255)), (596, 390))

    if ui_clickable: manager.draw_ui(window_surface)

def DisplayGenderSelect():

    LoadUI([male_button, female_button])

    RenderElement(selection_screen, (0,0))
    PlaceCentered(header_font.render("Who wood you like to date?", False, (255, 255, 255)), (480, 260))
    RenderElement(header_font.render("Female", False, (255, 255, 255)), (608, 330))
    RenderElement(header_font.render("Male", False, (255, 255, 255)), (290, 330))

    if ui_clickable: manager.draw_ui(window_surface)

def DisplayTextCard(text):

    LoadUI([])

    RenderElement(text_card, (0,0))
    PlaceMultiline(text, header_font, (255, 255, 255), (480, 280), 500, True)

def OnLoadTextCard():
    
    SchedualFunction(5, FadeToBlack, [1])
    SchedualFunction(6, ChangeScene, [DisplayMainGame, [], SetupRun])

def OnLoadWinTextCard():
    
    SchedualFunction(5, FadeToBlack, [1])
    SchedualFunction(6, ChangeScene, [DisplayTitleScreen, [], SomeFunc])

def DisplayScene(scene_func, args=[]):
    scene_func(*args)

active_scene = DisplayTitleScreen
active_scene_args = []

def ChangeScene(scene_func, args, load_func):
    global active_scene
    global active_scene_args

    FadeFromBlack(1)

    active_scene = scene_func
    active_scene_args = args

    load_func()

LoadMusic("DateOn.mp3")

while is_running:

    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            ProcessButtonClickFunctions(event.ui_element)
        
        manager.process_events(event)
    
    manager.update(time_delta)

    DisplayScene(active_scene, active_scene_args)

    FadeToFromBlack()
    UpdateClockSubscribers(time_delta)
    CheckFuncSchedual()

    pygame.display.update()