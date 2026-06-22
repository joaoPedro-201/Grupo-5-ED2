import spacy
import json
import os


def calculate_jaccard(set1, set2):
    """
    Calculates the Jaccard similarity index between two sets of words.
    """
    union = set1.union(set2)
    if not union:
        return 0.0
    return len(set1.intersection(set2)) / len(union)

class SpacyProcessor:
    def __init__(self):
        print("Carregando o modelo do spaCy (pt_core_news_sm)...")
        try:
            self.nlp = spacy.load("pt_core_news_sm")
        except OSError:
            print("Erro: Modelo não encontrado. Instale rodando no terminal:")
            print("python -m spacy download pt_core_news_sm")
            exit()

    def clean_text(self, text):
        """
        Analyzes the text, removes stopwords/punctuation, and extracts lowercase lemmas.
        """
        doc = self.nlp(text)
        
        # token.lemma_.lower() extracts the root of the word in lowercase
        important_words = [
            token.lemma_.lower() for token in doc 
            if not token.is_stop and not token.is_punct and not token.is_space
        ]
        
        return " ".join(important_words)

    def process_files(self, input_filename, output_filename):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        input_path = os.path.join(current_dir, "..", "dados", input_filename)
        output_path = os.path.join(current_dir, "..", "dados", output_filename)

        print(f"Lendo dados do JSON: {input_path}")
        
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
        except FileNotFoundError:
            print(f"ERRO: Arquivo não encontrado em {input_path}.")
            return

        for item in json_data:
            if 'texto' in item: 
                original_text = item['texto']
                # Applies cleaning and lemmatization
                item['texto_sumarizado'] = self.clean_text(original_text)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
            
        print(f"Processamento concluído com sucesso! Dados salvos em: {output_path}")

if __name__ == "__main__":
    processor = SpacyProcessor()
    
    processor.process_files("dataset.json", "resume_dataset.json")