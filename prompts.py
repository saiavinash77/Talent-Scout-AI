def technical_question_prompt(tech_stack: str, experience: str) -> str:
    """
    Generate technical interview questions based on tech stack
    and candidate experience level.
    """

    return f"""
You are a junior hiring assistant at a technology recruitment agency.

Candidate Details:
- Years of Experience: {experience}
- Tech Stack: {tech_stack}

Task:
Generate 3 to 5 technical interview questions tailored to the candidate's experience level.

Difficulty Guidelines:
- If experience is 0–1 years: basic fundamentals and simple concepts
- If experience is 2–4 years: intermediate concepts, practical usage, and best practices
- If experience is 5+ years: advanced concepts, system design thinking, performance, and real-world scenarios

Rules:
- Questions must be relevant to the listed tech stack
- Ask a mix of conceptual and practical questions
- Do NOT include answers
- Number each question clearly
- Keep questions concise and professional

Return ONLY the questions.
"""
