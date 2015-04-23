# -*- coding: utf-8 -*-

example_input =  ['Lesson 1: This is a Lesson Title' , 
                [['This is a Topic Header', 'This is a topic description with more words in it'], 
                 ['This is Another Topic Header', '', [['And this is a Subtopic Header', 'This is a subtopic description with more words in it'], 
                                                       ['This is Another Subtopic Header', 'This is another subtopic description with around the same number of words in it']]], 
                 ['This is an Additional Topic Header', 'This is just another topic description with some words in it']]]



def convert_notes_to_formatted_html(lesson_notes_to_format):
    append_formatted_html_here = ''
    html_with_lesson_title = append_formatted_html_here + add_html_formatting_to_lesson_title(get_lesson_title(lesson_notes_to_format))
    html_with_topics_and_subtopics = html_with_lesson_title + append_all_topics_html(get_all_lesson_topics_after_title(lesson_notes_to_format))
    ok_heres_your_html = html_with_topics_and_subtopics + formatted_lesson_closing_div_html()
    return ok_heres_your_html

def add_html_formatting_to_lesson_title(lesson_title):
    lesson_div = """\n
            <div class="lesson">"""
    lesson_title_h1 = """\n
                <h1>""" + lesson_title + '</h1>'
    lesson_title_formatted = lesson_div + lesson_title_h1
    return lesson_title_formatted

def get_lesson_title(lesson_notes_to_format):
    lesson_title = lesson_notes_to_format[0]
    return lesson_title

def append_all_topics_html(all_topics):
    all_topics_html = ''
    for each_topic in all_topics:
        current_topic_html = add_html_formatting_to_topic_title(topic_title_found_here(each_topic))
        if there_is_no_subtopic_in(each_topic):
            topic_description_html = add_html_formatting_to_topic_description(topic_description_found_here(each_topic))
            current_topic_html += topic_description_html
        else:
            current_topic_html += append_subtopic_html_with_or_without_topic_description(each_topic)
        current_topic_html += formatted_topic_closing_div()
        all_topics_html += current_topic_html
    return all_topics_html

def get_all_lesson_topics_after_title(lesson_notes_to_format): 
    all_topics = lesson_notes_to_format[1]
    return all_topics

def add_html_formatting_to_topic_title(topic_title):
    topic_div = """\n
                <div class="topic">"""
    topic_title_h2 = """\n
                    <h2>""" + topic_title + '</h2>'
    topic_title_formatted = topic_div + topic_title_h2
    return topic_title_formatted

def topic_title_found_here(current_topic):
    topic_title = current_topic[0]
    return topic_title

def there_is_no_subtopic_in(current_topic):
    if len(current_topic) == 2:
        return True
    else:
        return False

def topic_description_found_here(current_topic):
    topic_description = current_topic[1]
    return topic_description

def append_subtopic_html_with_or_without_topic_description(current_topic):
    if topic_description_is_not_empty(topic_description_found_here(current_topic)):
        topic_description_html = add_html_formatting_to_topic_description(topic_description_found_here(current_topic))
        topic_description_and_subtopic_html = topic_description_html + append_all_subtopic_html(current_topic)
        return topic_description_and_subtopic_html
    else:
        subtopic_html = append_all_subtopic_html(current_topic)
        return subtopic_html

def topic_description_is_not_empty(topic_description_placeholder):
    if topic_description_placeholder != '':
        return True
    else:
        return False

def add_html_formatting_to_topic_description(topic_description):
    topic_description_p = """\n
                    <p>""" + topic_description + '</p>'
    return topic_description_p

def append_all_subtopic_html(current_topic):
    all_subtopic_html = '' 
    all_subtopics = get_subtopics(current_topic)
    for each_subtopic in all_subtopics:
        each_subtopic_html = add_html_formatting_to_subtopic(subtopic_title_found_here(each_subtopic), subtopic_description_found_here(each_subtopic))
        all_subtopic_html += each_subtopic_html
    return all_subtopic_html

def get_subtopics(each_topic):
    all_subtopics = each_topic[2]
    return all_subtopics

def subtopic_title_found_here(current_subtopic):
    subtopic_title = current_subtopic[0]
    return subtopic_title

def subtopic_description_found_here(current_subtopic):
    subtopic_description = current_subtopic[1]
    return subtopic_description

def add_html_formatting_to_subtopic(subtopic_title, subtopic_description):
    subtopic_div = """\n
                    <div class="subtopic">"""
    subtopic_title_h3 = """\n
                        <h3>""" + subtopic_title + '</h3>'
    subtopic_description_p = """\n
                        <p>""" + subtopic_description + '</p>'
    subtopic_close_div = """\n
                    </div>"""
    subtopic_formatted = subtopic_div + subtopic_title_h3 + subtopic_description_p + subtopic_close_div
    return subtopic_formatted

def formatted_topic_closing_div():
    topic_close_div = """\n
                </div>"""
    return topic_close_div

def formatted_lesson_closing_div_html():
    lesson_closing_div = """\n
            </div>"""
    lesson_spacer = """\n
        <br/><!-- spacer -->"""
    lesson_closing_html_formatted = lesson_closing_div + lesson_spacer
    return lesson_closing_html_formatted


print convert_notes_to_formatted_html(example_input)




