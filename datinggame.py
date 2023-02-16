import pygame
import pygame_gui
import random

WINDOW_SIZE = (480*2, 270*2)

def SomeFunc(*params):
    print("first funnc")
    AddStrike()
    ChangeEmotion(0)
    

def SomeOtherFunc(*params):
    print("yet another func")
    ChangeEmotion(random.randint(1,3))

scenarios = [
            {'scenario': "Basically this thing happened what are you going to do about it you scared i bet your scared you scaredy cat",
            'option_a': {

                "text": "Option text that shows up in box",
                "positive_traits": ["affectionate", "attentive"],
                "negative_traits": ["stubborn"],
                "display_function": SomeFunc,
                "activation_function": SomeFunc,
                "display_func_params": [],
                "activation_func_params": []

            },
            'option_b': {

                "text": "Option text that shows up in box",
                "positive_traits": ["affectionate", "attentive"],
                "negative_traits": ["stubborn"],
                "display_function": SomeFunc,
                "activation_function": SomeOtherFunc,
                "display_func_params": [],
                "activation_func_params": []
            }}
            ]

              # Need Scenario text, traits that favor, traits that dont, stat features

pygame.init()

def LoadImage(image_name, scale=2):
    image = pygame.image.load(f"resources/images/{image_name}")
    print(f"Loaded {image_name}")
    return pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))




pygame.display.set_caption('Dating Game')
window_surface = pygame.display.set_mode(WINDOW_SIZE)

def PlaceCentered(element, pos, surface=window_surface):
    surface.blit(element, (pos[0] - (element.get_width() / 2), pos[1] - (element.get_height() / 2)))

def WriteOutText(text, font, color, timestep=0):
    '''This is meant to write out text sequentially, for now just make the text'''
    # write_out_string = ""
    # for char in text:
    #     write_out_string += char
    #     text_object = font.render(write_out_string, False, color)
    #     pygame.time.delay(timestep * 1000)

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
    # surf.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
    surf.fill(tint_color, None, pygame.BLEND_RGBA_MULT)
    return surf

    # while len(word_list) > 0:
    #     test_line = ""
    #     for word in word_list:
    #         test_line += word + " "
    #     text_render = font.render(test_line, False, color)
    #     if text.get_width() <= max_width:
    #         lines.append(text_render)

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

background = LoadImage("background.png")
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
        ExecuteSchedualedFunc(func, function_schedule[func])

        function_schedule.pop(func)
        clock_subs.pop(func)


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

manager = pygame_gui.UIManager(WINDOW_SIZE, "theme.json")

body_font = pygame.font.Font("Greenscr.ttf", 12)
header_font = pygame.font.Font("Greenscr.ttf", 20)

option_a_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((387, 215), (242, 245)),
                                            text='Option A Text',
                                            manager=manager)

option_b_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((640, 215), (242, 245)),
                                            text='Option B Text',
                                            manager=manager)

gender_preference = "male"

partner_traits_header = header_font.render("Traits", False, (255, 255, 255))

partner_name_text = "Gertrude's sister"

scenario_text = "Hey this thing happened"

option_a_text = "Yep he do be doin the do tho but what if i put a bunch of text here would it be too much to handle???"
option_b_text = "Oh boi there he go again"

current_player_stats = {'suave': 0, 'empathy': 0, 'quick-thinking': 0}
current_strikes = 0

current_traits = ["Quiet", "Smart", "Clean-freak", "Observant", "Scary", "Smooth"]

traits_texts = []

current_scenario = None

def SetupRun():
    CreateSO(gender_preference)

    global current_strikes
    current_strikes = 0

    LoadScenario(0)


def CheckFailState():
    if current_strikes >= 2:
        print("The game is lost")
        FadeToBlack(2)
        SchedualFunction(2, SetupRun)
        SchedualFunction(2, FadeFromBlack, [2])

def AddStrike():
    global current_strikes
    current_strikes += 1
    CheckFailState()





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
        traits_texts.append(body_font.render(trait.capitalize(), False, (255, 255, 255)))

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

ui_clickable = False

def ChangeUIClickable(clickable):

    global ui_clickable
    ui_clickable = clickable

def ProcessButtonClickFunctions(ui_button):

    if ui_clickable == False: return

    button_functions = {option_a_button: OptionA,
                        option_b_button: OptionB}
    button_functions[ui_button]()

FadeFromBlack(2)

clock = pygame.time.Clock()

# def AnimationController():

is_running = True

while is_running:

    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            ProcessButtonClickFunctions(event.ui_element)
        
        manager.process_events(event)
    
    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    
    DisplayDatePortrait(current_date_portrait)

    PlaceCentered(WriteOutText(partner_name_text, header_font, (255, 255, 200)), (230, 391))
    window_surface.blit(partner_traits_header, (188, 420))
    PlaceMultiline(scenario_text, header_font, (20, 20, 20), (410, 50), 400)
    PlaceMultiline(option_a_text, header_font, (20, 20, 20), (512, 236), 200, True)
    PlaceMultiline(option_b_text, header_font, (20, 20, 20), (762, 236), 200, True)
    window_surface.blit(suave_icon, (390, 464))
    window_surface.blit(empathy_icon, (560, 464))
    window_surface.blit(quickthinking_icon, (730, 464))
    ShowEmotion()
    ShowStrikes(current_strikes)
  

    for index in range(len(traits_texts)):
        if index < 3:
            window_surface.blit(traits_texts[index], (110, 456 + (index * 22)))
        else:
            window_surface.blit(traits_texts[index], (240, 456 + ((index - 3) * 22)))

    manager.draw_ui(window_surface)

    FadeToFromBlack()
    UpdateClockSubscribers(time_delta)
    CheckFuncSchedual()

    pygame.display.update()