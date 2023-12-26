from typing import Any
from django.core.management import BaseCommand
from core.models import Town, State

nigerian_states = {
    'Lagos': ['Lagos', 'Ikeja', 'Victoria Island', 'Surulere', 'Lekki'],
    'Kano': ['Kano', 'Dala', 'Gwale', 'Fagge', 'Kumbotso'],
    'Oyo': ['Ibadan', 'Ogbomosho', 'Iseyin', 'Saki', 'Eruwa'],
    'Rivers': ['Port Harcourt', 'Obio-Akpor', 'Ikwerre', 'Eleme', 'Oyigbo'],
    'Kaduna': ['Kaduna', 'Zaria', 'Sabon Gari', 'Kafanchan', 'Makarfi'],
    'Katsina': ['Katsina', 'Daura', 'Funtua', 'Malumfashi', 'Mani'],
    'Delta': ['Asaba', 'Warri', 'Sapele', 'Ughelli', 'Kwale'],
    'Ogun': ['Abeokuta', 'Ijebu-Ode', 'Sagamu', 'Ilaro', 'Ota'],
    'Jigawa': ['Dutse', 'Hadejia', 'Birnin Kudu', 'Kazaure', 'Gumel'],
    'Kwara': ['Ilorin', 'Offa', 'Kaiama', 'Jebba', 'Omu-Aran'],
    'Benue': ['Makurdi', 'Gboko', 'Otukpo', 'Adikpo', 'Katsina-Ala'],
    'Sokoto': ['Sokoto', 'Tambuwal', 'Wurno', 'Goronyo', 'Isa'],
    'Anambra': ['Awka', 'Onitsha', 'Nnewi', 'Aguata', 'Orumba'],
    'Bauchi': ['Bauchi', 'Azare', 'Misau', 'Jamaare', 'Darazo'],
    'Enugu': ['Enugu', 'Nsukka', 'Nsukka', 'Agbani', 'Awgu'],
    'Osun': ['Osogbo', 'Ile-Ife', 'Iwo', 'Ede', 'Ikire'],
    'Nasarawa': ['Lafia', 'Keffi', 'Akwanga', 'Nasarawa', 'Toto'],
    'Kebbi': ['Birnin Kebbi', 'Argungu', 'Yauri', 'Zuru', 'Jega'],
    'Bayelsa': ['Yenagoa', 'Brass', 'Ogbia', 'Nembe', 'Sagbama'],
    'Imo': ['Owerri', 'Orlu', 'Okigwe', 'Mbaise', 'Nkwerre'],
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        for state, towns in nigerian_states.items():
            st, _ = State.objects.get_or_create(name=state)
            for town in towns:
                Town.objects.get_or_create(state=st, name=town)
        print("--------done---------")
                