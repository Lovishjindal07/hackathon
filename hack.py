#Define SKILL_ALIASES dictionary
SKILL_ALIASES = {
    "machine learning": ["ml", "deep learning"],
    "data science": ["ds", "data analytics"],
    "web development": ["web dev", "full stack"],
    "python programming": ["python", "py"],
    # Add more aliases as needed
}

def normalizeskills(rawskills):
    """
    Normalize raw skills using SKILL_ALIASES.

    Args:
    raw_skills (str): Comma-separated raw skills.

    Returns:
    list: List of normalized, canonical skills.
    """
    # Split skills by comma and convert to lowercase
    skills = [skill.strip().lower() for skill in raw_skills.split(",")]

    # Match multi-word phrases first
    canonical_skills = []
    for skill in skills:
        # Check if skill is a multi-word phrase
        if " " in skill:
            # Check if skill is in SKILL_ALIASES
            if skill in SKILL_ALIASES:
                # Add canonical skill
                canonical_skills.append(skill)
            else:
                # Check if skill is an alias
                for canonical, aliases in SKILL_ALIASES.items():
                    if skill in aliases:
                        # Add canonical skill
                        canonical_skills.append(canonical)
                        break
        else:
            # Check if skill is in SKILL_ALIASES
            if skill in [alias for aliases in SKILL_ALIASES.values() for alias in aliases]:
                # Find canonical skill
                for canonical, aliases in SKILL_ALIASES.items():
                    if skill in aliases:
                        # Add canonical skill
                        canonical_skills.append(canonical)
                        break
            elif skill in SKILL_ALIASES:
                # Add canonical skill
                canonical_skills.append(skill)

    # Discard unknown tokens and deduplicate canonical skills
    normalized_skills = list(set(canonical_skills))

    return normalized_skills

# Example usage
raw_skills = "Machine Learning, ML, Data Science, DS, Web Development, Full Stack, Python Programming, Python, Py, Unknown Skill"
normalizedskills = normalizeskills(raw_skills)
print(normalizedskills)



import numpy as np
import math

#Define the list of normalized resume skills
#Each inner list represents a resume
resumes = [
    ["machine learning", "data science", "web development"],
    ["machine learning", "python programming", "data science"],
    ["web development", "full stack", "python programming"],
    ["data science", "machine learning", "data analytics"],
    ["python programming", "web development", "full stack"],
    ["machine learning", "data science", "python programming"],
    ["web development", "data science", "full stack"],
    ["python programming", "machine learning", "web development"],
    ["data science", "python programming", "data analytics"],
    ["full stack", "web development", "machine learning"]
]

#Build shared vocabulary from all normalized resume skills, sorted alphabetically
vocabulary = sorted(set([skill for resume in resumes for skill in resume]))

#Compute df for each skill
df = {skill: sum(1 for resume in resumes if skill in resume) for skill in vocabulary}

#Calculate TF-IDF vectors for each resume
tfidfvectors = []
for resume in resumes:
    unique_skills = set(resume)
    N = len(unique_skills)
    tfidfvector = [0.0] * len(vocabulary)
    for i, skill in enumerate(vocabulary):
        if skill in unique_skills:
            tf = 1 / N
            idf = math.log(10 / df[skill])
            tfidfvector[i] = tf * idf
    tfidfvectors.append(tfidfvector)

#Print the TF-IDF vectors for each resume
for i, vector in enumerate(tfidfvectors):
    print(f"Resume {i+1} TF-IDF Vector: {vector}")

#Print the vocabulary and df for reference
print("\nVocabulary:")
for i, skill in enumerate(vocabulary):
    print(f"{i+1}. {skill} (df: {df[skill]})")





import numpy as np
import math

#Define the list of normalized resume skills
#Each inner list represents a resume
resumes = [
    ["machine learning", "data science", "web development"],
    ["machine learning", "python programming", "data science"],
    ["web development", "full stack", "python programming"],
    ["data science", "machine learning", "data analytics"],
    ["python programming", "web development", "full stack"],
    ["machine learning", "data science", "python programming"],
    ["web development", "data science", "full stack"],
    ["python programming", "machine learning", "web development"],
    ["data science", "python programming", "data analytics"],
    ["full stack", "web development", "machine learning"]
]

#Build shared vocabulary from all normalized resume skills, sorted alphabetically
vocabulary = sorted(set([skill for resume in resumes for skill in resume]))
print("Shared Vocabulary:")
print(vocabulary)

#Compute df for each skill
df = {skill: sum(1 for resume in resumes if skill in resume) for skill in vocabulary}
print("\nDocument Frequency (df):")
for skill, freq in df.items():
    print(f"{skill}: {freq}")

#Calculate TF-IDF vectors for each resume
tfidfvectors = []
for i, resume in enumerate(resumes):
    unique_skills = set(resume)
    N = len(unique_skills)
    tfidfvector = []
    for skill in vocabulary:
        if skill in unique_skills:
            tf = 1 / N
            idf = math.log(10 / df[skill])
            tf_idf = tf * idf
            tfidfvector.append(tf_idf)
        else:
            tfidfvector.append(0.0)
    tfidfvectors.append(tfidfvector)

#Print the TF-IDF vectors for each resume
print("\nTF-IDF Vectors:")
for i, vector in enumerate(tfidfvectors):
    print(f"Resume {i+1}: {vector}")

#Print the TF-IDF vectors in a matrix format
print("\nTF-IDF Matrix:")
for i, vector in enumerate(tfidfvectors):
    print(f"Resume {i+1}: {[round(x, 4) for x in vector]}")

#Calculate the TF-IDF matrix using NumPy
tfidfmatrix = np.array(tfidfvectors)
print("\nTF-IDF Matrix (NumPy):")
print(tfidfmatrix)



import numpy as np
import math

#Define the SKILL_ALIASES dictionary
SKILL_ALIASES = {
    "machine learning": ["ml", "deep learning"],
    "data science": ["ds", "data analytics"],
    "web development": ["web dev", "full stack"],
    "python programming": ["python", "py"],
    # Add more aliases as needed
}

#efine the list of normalized resume skills
#Each inner list represents a resume
resumes = [
    ["machine learning", "data science", "web development"],
    ["machine learning", "python programming", "data science"],
    ["web development", "full stack", "python programming"],
    ["data science", "machine learning", "data analytics"],
    ["python programming", "web development", "full stack"],
    ["machine learning", "data science", "python programming"],
    ["web development", "data science", "full stack"],
    ["python programming", "machine learning", "web development"],
    ["data science", "python programming", "data analytics"],
    ["full stack", "web development", "machine learning"]
]

#Define the list of JD skills
#Each inner list represents a JD
jds = [
    ["machine learning", "data science", "python programming"],
    ["web development", "full stack", "javascript"],
    ["data science", "machine learning", "sql"],
    ["python programming", "web development", "django"],
    ["full stack", "web development", "react"]
]

#Build shared vocabulary from all normalized resume skills, sorted alphabetically
vocabulary = sorted(set([skill for resume in resumes for skill in resume]))
print("Shared Vocabulary:")
print(vocabulary)

#ormalize JD skills using SKILL_ALIASES
normalized_jds = []
for jd in jds:
    normalized_jd = []
    for skill in jd:
        if " " in skill:
            if skill in SKILL_ALIASES:
                normalized_jd.append(skill)
            else:
                for canonical, aliases in SKILL_ALIASES.items():
                    if skill in aliases:
                        normalized_jd.append(canonical)
                        break
        else:
            if skill in [alias for aliases in SKILL_ALIASES.values() for alias in aliases]:
                for canonical, aliases in SKILL_ALIASES.items():
                    if skill in aliases:
                        normalized_jd.append(canonical)
                        break
            elif skill in SKILL_ALIASES:
                normalized_jd.append(skill)
    normalizedjds.append(normalizedjd)

#Build binary vectors for each JD over the shared vocabulary
jdbinaryvectors = []
for jd in normalized_jds:
    binary_vector = [1 if skill in jd else 0 for skill in vocabulary]
    jdbinaryvectors.append(binary_vector)

#Compute TF-IDF vectors for each resume
tfidfvectors = []
for i, resume in enumerate(resumes):
    unique_skills = set(resume)
    N = len(unique_skills)
    tfidfvector = []
    for skill in vocabulary:
        if skill in unique_skills:
            tf = 1 / N
            df = sum(1 for r in resumes if skill in r)
            idf = math.log(10 / df)
            tf_idf = tf * idf
            tfidfvector.append(tf_idf)
        else:
            tfidfvector.append(0.0)
    tfidfvectors.append(tfidfvector)

#Compute cosine similarity between each resume TF-IDF vector and each JD binary vector
similarities = []
for i, tfidfvector in enumerate(tfidfvectors):
    resume_similarities = []
    for j, jdbinaryvector in enumerate(jdbinaryvectors):
        dotproduct = sum(a * b for a, b in zip(tfidfvector, jdbinary_vector))
        magnitudetfidf = math.sqrt(sum(a  2 for a in tfidfvector))
        magnitudejdbinary = math.sqrt(sum(a  2 for a in jdbinaryvector))
        cosinesimilarity = dotproduct / (magnitudetfidf  magnitudejdbinary) if magnitudetfidf  magnitudejdbinary != 0 else 0
        resumesimilarities.append((j, round(cosinesimilarity, 2)))
    similarities.append(resume_similarities)

#Rank top 3 candidates per JD with scores rounded to 2 decimal places and alphabetical tie-breaking
for i, jd in enumerate(jds):
    jd_similarities = [similarity for similarity in similarities if similarity[i][0] == i]
    rankedcandidates = sorted(jdsimilarities, key=lambda x: (-x[1][1], resumes[x[0]].str()))
    print(f"JD {i+1}: {jd}")
    for candidate in ranked_candidates[:3]:
        print(f"  - Resume {candidate[0]+1}: {resumes[candidate[0]]} (Score: {candidate[1][1]})")
    print()