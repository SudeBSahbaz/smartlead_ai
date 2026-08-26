import requests

from config import Config


class AIServiceError(Exception):
    """
    Yapay zekâ servisiyle ilgili kontrollü hatalar.
    """


class AIService:
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.business_context = Config.BUSINESS_CONTEXT

        self.api_url = (
            "https://api.groq.com/openai/v1/chat/completions"
        )

        # Yönergede verilen llama-3.1-8b-instant modeli
        # Groq Developer katmanında artık çalışmadığı için
        # güncel çalışan model kullanılır.
        self.model = "openai/gpt-oss-20b"

    def _system_mesaji_olustur(self):
        """
        Sistem mesajını BUSINESS_CONTEXT üzerinden oluşturur.
        """
        return self.business_context.strip()

    def yanit_uret(
        self,
        mesaj,
        gecmis=None,
    ):
        """
        Kullanıcı mesajını yapay zekâ servisine gönderir
        ve metin yanıtını döndürür.
        """

        if not self.api_key:
            return (
                "SmartLead AI şu anda demo modunda çalışıyor. "
                "Yapay zekâ bağlantısı henüz yapılandırılmamış."
            )

        if gecmis is None:
            gecmis = []

        messages = [
            {
                "role": "system",
                "content": self._system_mesaji_olustur(),
            }
        ]

        for item in gecmis:
            if (
                isinstance(item, dict)
                and item.get("role")
                in {
                    "user",
                    "assistant",
                }
                and item.get("content")
            ):
                messages.append(
                    {
                        "role": item["role"],
                        "content": str(
                            item["content"]
                        ),
                    }
                )

        messages.append(
            {
                "role": "user",
                "content": mesaj,
            }
        )

        try:
            response = requests.post(
                self.api_url,
                headers={
                    "Authorization":
                        f"Bearer {self.api_key}",
                    "Content-Type":
                        "application/json",
                },
                json={
                    "model":
                        self.model,
                    "messages":
                        messages,
                    "temperature":
                        0.3,
                },
                timeout=45,
            )

            response.raise_for_status()

            data = response.json()

            return (
                data["choices"][0]
                ["message"]
                ["content"]
            )

        except requests.RequestException as error:
            raise AIServiceError(
                "Yapay zekâ servisine bağlanırken "
                "bir hata oluştu."
            ) from error

        except (
            KeyError,
            IndexError,
            TypeError,
            ValueError,
        ) as error:
            raise AIServiceError(
                "Yapay zekâ servisinden "
                "beklenmeyen bir yanıt alındı."
            ) from error


ai_service = AIService()