def formatted_lesson_title_html(lesson_title):
    lesson_div = """
<div class="lesson">"""
    lesson_title_h1 = """
    <h1>""" + lesson_title + '</h1>'
    lesson_title_formatted = lesson_div + lesson_title_h1
    return lesson_title_formatted


#the topic html functions will operate inside of a for loop
def formatted_topic_title_html(topic_title):
    topic_div = """
            <div class="topic">"""
    topic_title_h2 = """
                <h2>""" + topic_title + '</h2>'
    topic_title_formatted = topic_div + topic_title_h2
    return topic_title_formatted


def formatted_topic_description_html(topic_description):
    topic_description_p = """
                    <p>""" + topic_description + '</p>'
    return topic_description_p


#formatted_sub_topic_html will also operate within a for loop 
def formatted_sub_topic_html(sub_topic_title, sub_topic_description):
    sub_topic_div = """
                        <div class="sub_topic">"""
    sub_topic_title_h3 = """
                            <h3>""" + sub_topic_title + '</h3>'
    sub_topic_description_p = """
                                <p>""" + sub_topic_description + '</p>'
    sub_topic_close_div = """
                        </div>"""
    sub_topic_formatted = sub_topic_div + sub_topic_title_h3 + sub_topic_description_p + sub_topic_close_div
    return sub_topic_formatted


def formatted_topic_closing_div():
    topic_close_div = """
            </div>"""
    return topic_close_div


def formatted_lesson_closing_div_html():
    lesson_closing_div = """
</div>"""
    lesson_spacer = """
    <br/><!-- spacer -->"""
    lesson_closing_html_formatted = lesson_closing_div + lesson_spacer
    return lesson_closing_html_formatted


def get_lesson_contents(lesson_notes_list): 
    all_topics = lesson_notes_list[1]
    return all_topics


def get_sub_topics(each_topic):
    all_sub_topics = each_topic[2]
    return all_sub_topics


sample_input =  ['Lesson 1: This is a Lesson Title' , 
                [['This is a Topic Header', 'This is a topic description with more words in it'], 
                 ['This is Another Topic Header', '', [['And this is a Subtopic Header', 'This is a subtopic description with more words in it'], 
                                                       ['This is Another Subtopic Header', 'This is another subtopic description with around the same number of words in it']]], 
                 ['This is an Additional Topic Header', 'This is just another topic description with some words in it']]]

# example notes structure:
# [lesson title [lesson notes]]
#                [lesson notes] --> [[topic title, topic description], [topic title, topic description], [topic title, empty string '' or topic description, [[subtopic title, subtopic description], [subtopic title, subtopic description]]]



# I didn't want to have another nested loop inside the main make_me_some_html function below, so I 
# abstracted the function that concatenates the sub topic html: 
def add_all_sub_topic_html(all_sub_topics):
    all_sub_topic_html = '' 
    for each_sub_topic in all_sub_topics:
        sub_title = each_sub_topic[0]
        sub_description = each_sub_topic[1]
        each_sub_topic_html = formatted_sub_topic_html(sub_title, sub_description)
        all_sub_topic_html += each_sub_topic_html
    return all_sub_topic_html



def make_me_some_html(lesson_notes_list):
    # Here's where we will append our html:
    ok_heres_your_html = ''
    # Generate the lesson title html, stopping before the first topic:
    lesson_title = lesson_notes_list[0]
    title_html = formatted_lesson_title_html(lesson_title)
    ok_heres_your_html += title_html
    all_lesson_topics = get_lesson_contents(lesson_notes_list)
    # Now we concatenate all of the topics, one at a time:
    for each_topic in all_lesson_topics:
        # Starting with the title:
        topic_title = each_topic[0]
        topic_title_html = formatted_topic_title_html(topic_title)
        ok_heres_your_html += topic_title_html
        topic_description = each_topic[1]
        # A topic that does not contain sub-topics will be of length == 2. When that 
        # is the case, we add the description and then move to the next topic in the loop:
        if len(each_topic) == 2:
            topic_description_html = formatted_topic_description_html(topic_description)
            ok_heres_your_html += topic_description_html
        # If topic length is > 2, then we need to add its sub-topics:
        else:
            # Sometimes, there is still a topic description before the sub-topic title:
            if topic_description != '':
                topic_description_html = formatted_topic_description_html(topic_description)
                ok_heres_your_html += topic_description_html
                all_sub_topics = get_sub_topics(each_topic)
                sub_topic_html = add_all_sub_topic_html(all_sub_topics)
                ok_heres_your_html += sub_topic_html
            # In other cases, the first sub-topic title immediately proceeds the topic title:
            else:
                all_sub_topics = get_sub_topics(each_topic)
                sub_topic_html = add_all_sub_topic_html(all_sub_topics)
                ok_heres_your_html += sub_topic_html
        # topic closing divs inside of loop:
        ok_heres_your_html += formatted_topic_closing_div()
    # lesson closing div outside of loop:
    ok_heres_your_html += formatted_lesson_closing_div_html()
    return ok_heres_your_html











