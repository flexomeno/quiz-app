import uuid

def parse_gift_file(content):
    questions = []
    blocks = content.strip().split('\n\n')
    
    for block in blocks:
        lines = block.strip().split('\n')
        question_text = lines[0].replace('::', '').strip()
        answers = []
        
        for line in lines[1:]:
            correct = line.startswith('=')
            answer_text = line.replace('=', '').replace('~', '').strip()
            answers.append({'text': answer_text, 'correct': correct})
        
        questions.append({
            'id': str(uuid.uuid4()),
            'question': question_text,
            'answers': answers
        })
    
    return questions
