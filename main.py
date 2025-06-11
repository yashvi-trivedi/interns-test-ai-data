import argparse
from csv_reader import read_subject_csv
import csv

import os
from dotenv import load_dotenv

def get_concept_dict(subject):
    if subject == "math":
        concept_dict = {
        "profit & loss": ["selling price", "profit", "overall profit", "loss"],
        "percentages": ["% more", "% less", "range of values", "percentage", "percent", "%"],
        "algebraic ratio problems": ["x% more", "x% of sum", "value of x"],
        "profit & loss & discount": ["discount"],
        "simple interest": ["simple interest"],
        "compound interest": ["compound interest", "compounded"],
        "work & efficiency": ["time", "work", "efficiency", "combined", "percentage"],
        "investment & profit sharing": ["investment"],
        "unitary method & proportions": ["twice the price", "times", "percentage", "weight", "length"],
        "combinatorics": ["whole numbers", "triplets", "sum is 10", "ordered triplets"],
        "probability": ["die", "cards", "dice", "head", "heads", "tails", "tail"]
    }
    elif subject == "physics":
        concept_dict = {
        "point charges": ["charged bodies", "small size compared to distance"],
        "dielectric constant": ["dielectric constant", "permittivity", "metal"],
        "electric field lines": ["field strength", "field direction", "nature of charge", "electric field lines"],
        "conservative electric field": ["closed path", "unit positive test charge", "work done", "electric field"],
        "charging by friction": ["glass rod", "silk", "rubbing", "electrons", "triboelectric"],
        "torque on dipole in magnetic field": ["work done", "rotating dipole", "θ1", "θ2", "magnetic field"],
        "magnetic dipole moment": ["magnetic dipole moment", "formula", "current", "area"],
        "earth’s magnetic field": ["freely suspended magnet", "north-south direction", "magnetic poles"],
        "power factor in ac circuits": ["power factor", "resistive circuit", "unity", "rlc"],
        "resonance in lcr circuit": ["lcr circuit", "resonance", "impedance minimum", "current maximum"],
        "interference pattern": ["fringe width", "young's double slit", "coherent sources", "wavelength"],
        "polarization": ["transverse nature of light", "polarization", "polaroid", "glasses", "sunglasses"],
        "limitations of wave theory": ["wave theory", "photoelectric effect", "blackbody radiation"],
        "principle of superposition": ["interference", "light waves", "energy conservation"],
        "lens wavefront transformation": ["convex lens", "plane wave", "wavefront", "spherical shape"],
        "beta decay": ["beta particle", "parent nucleus", "daughter nucleus", "atomic number change"],
        "gamma decay": ["gamma decay", "energy level", "no change in mass", "excited nucleus"],
        "isotones": ["isotones", "same number of neutrons"],
        "em wave phase": ["phase difference", "electric field", "magnetic field", "electromagnetic wave"]
    }
    elif subject == "economics":
        concept_dict = {
        "monetary policy & central banking": [
            "interest rate hike", "monetary policy", "inflation control", "consumer prices",
            "central bank", "liquidity", "sterilization", "money supply", "repo rate",
            "reverse repo", "laf", "call money market", "treasury bills"
        ],

        "digital currency": [
            "digital rupee", "rbi digital currency", "central bank digital currency",
            "sovereign currency", "monetary policy", "convertibility", "rbi liability"
        ],

        "banking & financial regulation": [
            "syndicated lending", "credit line", "multiple lenders", "foreign banks",
            "capital requirement", "banking subsidiary", "indian nationals",
            "nbfc", "g-secs", "stock exchanges", "foreign institutional investors",
            "corporate bonds", "csr", "priority sector", "bank loans"
        ],

        "capital markets & instruments": [
            "g-secs", "stock market", "bond market", "etf", "financial instruments",
            "corporate bonds", "collateral borrowing", "lending obligations",
            "invits", "infrastructure investment trust", "dividends", "interest income"
        ],

        "indian economy & policy": [
            "minimum support price", "niger seeds", "tribal farming", "kharif crop",
            "digital india land records", "transliteration", "cadastral maps",
            "economic sectors", "primary", "secondary", "tertiary", "physical capital",
            "fixed capital", "working capital", "msme", "production linked incentive"
        ],

        "trade & global economics": [
            "india exports", "global exports", "foreign trade", "usa debt default",
            "treasury bonds", "currency swap", "foreign companies",
            "brand recognition", "intangible investments"
        ],

        "agricultural marketing and prices": ["small farmer large field"]
    }
    
    elif subject == "ancient_history":
        concept_dict = {
        "indus valley civilization": [
            'harappan', 'indus', 'indus valley', 'the indus valley civilization', 'a harappan site',
            'cotton', 'textiles', 'copper artefacts', 'horse-drawn chariots', 'secular civilization',
            'male and female deities', 'rock-cut shrines', 'urban planning', 'terracotta art'
        ],
        "vedic and later vedic period": [
            'early vedic aryans', 'vedic aryans', 'the religion', 'rituals', 'penance', 'enjoyment',
            'indifference', 'extremities', 'vedas'
        ],
        "buddhism and jainism": [
            'jain', 'the jain philosophy', 'aryadeva jaina', 'dignaga buddhist', 'jainism',
            'other sects', 'his religious sect', 'his own sect', 'excessive devotion'
        ],
        "mauryan empire and ashoka": [
            'ashoka', 'king ashoka', 'ranyo ashoka', 'emperor ashoka', 'the edicts', 'stone portrait',
            'relief sculpture inscriptions', 'the following rulers', 'his subjects', 'this inscription'
        ],
        "gupta period": [
            'gupta', 'guptas', 'the gupta dynasty', 'the gupta period', 'vishti', 'forced labour',
            'connected reservoirs', 'management'
        ],
        "historical geography and towns": [
            'burzahom', 'kanauj', 'malwa', 'thanesar', 'valabhi', 'devagiri', 'chaul', 'ghantasala', 'kadura',
            'ganeshwar', 'chandra - ketugarh'
        ],
        "ancient education and land systems": [
            'single brahmin', 'villages', 'colleges', 'eripatti : land revenue', 'taniyurs', 'dronavapa',
            'kulyavapa', 'land grants'
        ],
        "ancient texts and literature": [
            'arthashastra', 'kautilya', 'kautilyas arthashastra', 'parishishta parvan',
            'trishashtilakshana mahapurana', 'avadanasataka', 'nettipakarana', 'kalidasa',
            'panini', 'amarasimha', 'bhavabhuti', 'hastimalla', 'kshemeshvara'
        ],
        "foreign travelers and trade": [
            'hiuen tsang', 'yuan chwang', 'river routes', 'barrier stations', 'southeast asia',
            'bay of bengal', 'maritime history', 'trade links'
        ],
        "science and technology in ancient india": [
            'specialised surgical instruments', 'internal organs', 'different kinds', 'common use'
        ],
        "political and administrative systems": [
            'judicial powers', 'guild', 'chief administrative authority', 'rules', 'standards',
            'duties', 'ordeals', 'fire', 'poison', 'water'
        ],
        "chronicles and dynastic histories": [
            'dynastic histories', 'epic tales', 'chronicles', 'the memorising', 'the profession',
            'pushyamitra shunga', 'chandra gupta-ii', 'harshavardhana'
        ]
    }
    else:
        raise ValueError("Incorrect subject name")
    
    return concept_dict

def match_concepts(question, concept_dict):
    # Load .env
    load_dotenv()
    USE_LLM = os.getenv("ANTHROPIC_API_KEY") 
    if USE_LLM == "your_anthropic_api_key_here":
        # Match concepts from dictionary if the value of API key is default phrase
        # API_KEY=your_anthropic_api_key_here => key not entered
        matches = []
        q_lower = question.lower()
        for concept, keywords in concept_dict.items():
            for keyword in keywords:
                if keyword in q_lower:
                    matches.append(concept)
                    break
        return matches or ["Uncategorized"]

    else:
        # Uses LLM-based mapping
        
        from llm_api import call_anthropic  # Deferred import
        prompt=f"Identify the key concepts being tested in the following question and give a list of high-level concepts only.: {question}"
        response = call_anthropic(prompt)
        return [concept.strip() for concept in response.split(",")]


def main():
    parser = argparse.ArgumentParser(description="Intern Test Task: Question to Concept Mapping")
    parser.add_argument('--subject', required=True, choices=['ancient_history', 'math', 'physics', 'economics'], help='Subject to process')
    args = parser.parse_args()

    data = read_subject_csv(args.subject)
    print(f"Loaded {len(data)} questions for subject: {args.subject}")
    
    # --- PLACEHOLDER FOR USER CODE ---
    concept_dict = get_concept_dict(args.subject)
    
    with open("output_concepts.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Question Number", "Question", "Concepts"])

        for row in data:
            q_no = row.get("Question Number", "")
            question = row.get("Question", "")
            concepts = match_concepts(question, concept_dict)
            writer.writerow([q_no, question, "; ".join(concepts)])
            print(f"Q{q_no}: {concepts}")   
    # ----------------------------------

if __name__ == "__main__":
    main()