# Projeto de Análise e Projeto de Sistemas (IF718)

A Level Up é uma plataforma que auxilia no desenvolvimento pessoal e profissional de colaboradores de uma empresa através da construção de mapas de desenvolvimento individual baseados em recomendação de habilidades desejadas pelo colaborador.


## Equipe

* Carolina Cruz (ccal2)
* Gabriela Leal (gmfl)
* Rosinaldo Guedes (rglj2)

## Entregas

* [Escopo do projeto](/Escopo.pdf)
* [Apresentação RUP](/RUP/Apresentação.pdf)
* [Diagramas SOA](https://drive.google.com/file/d/1n4LM_RC1Pw5MWZd_4e3yhd5xs7xC13u-/view?usp=sharing)
* [Apresentação SOA + correções RUP](https://docs.google.com/presentation/d/1DOvZDRH0CWuSSsYQl52Nd6PiGaDszgyCDNqaptMIytM/edit?usp=sharing)


## Rodar Projeto
### RUP
```bash
cd RUP
pip3 install -r requirements.txt # Se for a primeira vez
python3 app/main.py
```

### SOA
```bash
cd SOA
docker-compose build # Se for a primeira vez
docker-compose up
```
