import hashlib

class SurrogateKeyGenerator:
    def __init__(self, salt=""):
        """
        Inicializa o gerador de surrogate key.
        O salt pode ser usado para garantir que os hashes sejam únicos.
        """
        self.salt = salt

    def generate_surrogate_key(self, id_value):
        """
        Gera uma surrogate key baseada no hash do valor do ID original.
        :param id_value: Valor do ID que será mascarado.
        :return: Surrogate key (hash) do ID.
        """
        # Converte o ID para string e concatena com o salt
        id_str = str(id_value) + self.salt
        
        # Gera o hash SHA-256
        hash_object = hashlib.sha256(id_str.encode())
        surrogate_key = hash_object.hexdigest()
        
        # Retorna uma versão truncada da chave para simplificação (opcional)
        return surrogate_key[:16]  # Trunca para 16 caracteres
