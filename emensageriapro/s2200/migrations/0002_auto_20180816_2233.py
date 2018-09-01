# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2200', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2200afastamento',
            name='codmotafast',
            field=models.CharField(max_length=2, choices=[(b'01', '01 - Acidente/Doen\xe7a do trabalho'), (b'03', '03 - Acidente/Doen\xe7a n\xe3o relacionada ao trabalho'), (b'05', '05 - Afastamento/licen\xe7a prevista em regime pr\xf3prio (estatuto), sem remunera\xe7\xe3o'), (b'06', '06 - Aposentadoria por invalidez'), (b'07', '07 - Acompanhamento - Licen\xe7a para acompanhamento de membro da fam\xedlia enfermo'), (b'08', '08 - Afastamento do empregado para participar de atividade do Conselho Curador do FGTS - art. 65, \xa76\xba, Dec. 99.684/90 (Regulamento do FGTS)'), (b'10', '10 - Afastamento/licen\xe7a prevista em regime pr\xf3prio (estatuto), com remunera\xe7\xe3o'), (b'11', '11 - C\xe1rcere'), (b'12', '12 - Cargo Eletivo - Candidato a cargo eletivo - Lei 7.664/1988. art. 25\xb0, par\xe1grafo \xfanico - Celetistas em geral'), (b'13', '13 - Cargo Eletivo - Candidato a cargo eletivo - Lei Complementar 64/1990. art. 1\xb0, inciso II, al\xednea 1 - Servidor p\xfablico, estatut\xe1rio ou n\xe3o, dos \xf3rg\xe3os ou entidades da Administra\xe7\xe3o Direta ou Indireta da Uni\xe3o, dos Estados, do Distrito Federal, dos Muni (...)'), (b'14', '14 - Cess\xe3o / Requisi\xe7\xe3o'), (b'15', '15 - Gozo de f\xe9rias ou recesso - Afastamento tempor\xe1rio para o gozo de f\xe9rias ou recesso'), (b'16', '16 - Licen\xe7a remunerada - Lei, liberalidade da empresa ou Acordo/Conven\xe7\xe3o Coletiva de Trabalho'), (b'17', '17 - Licen\xe7a Maternidade - 120 dias e suas prorroga\xe7\xf5es/antecipa\xe7\xf5es, inclusive para o c\xf4njuge sobrevivente'), (b'18', '18 - Licen\xe7a Maternidade - 121 dias a 180 dias, Lei 11.770/2008 (Empresa Cidad\xe3), inclusive para o c\xf4njuge sobrevivente'), (b'19', '19 - Licen\xe7a Maternidade - Afastamento tempor\xe1rio por motivo de aborto n\xe3o criminoso'), (b'20', '20 - Licen\xe7a Maternidade - Afastamento tempor\xe1rio por motivo de licen\xe7a-maternidade decorrente de ado\xe7\xe3o ou guarda judicial de crian\xe7a, inclusive para o c\xf4njuge sobrevivente'), (b'21', '21 - Licen\xe7a n\xe3o remunerada ou Sem Vencimento'), (b'22', '22 - Mandato Eleitoral - Afastamento tempor\xe1rio para o exerc\xedcio de mandato eleitoral, sem remunera\xe7\xe3o'), (b'23', '23 - Mandato Eleitoral - Afastamento tempor\xe1rio para o exerc\xedcio de mandato eleitoral, com remunera\xe7\xe3o'), (b'24', '24 - Mandato Sindical - Afastamento tempor\xe1rio para exerc\xedcio de mandato sindical'), (b'25', '25 - Mulher v\xedtima de viol\xeancia - Lei 11.340/2006 - art. 9\xba \xa72o, II - Lei Maria da Penha'), (b'26', '26 - Participa\xe7\xe3o de empregado no Conselho Nacional de Previd\xeancia Social-CNPS (art. 3\xba, Lei 8.213/1991)'), (b'27', '27 - Qualifica\xe7\xe3o - Afastamento por suspens\xe3o do contrato de acordo com o art 476-A da CLT'), (b'28', '28 - Representante Sindical - Afastamento pelo tempo que se fizer necess\xe1rio, quando, na qualidade de representante de entidade sindical, estiver participando de reuni\xe3o oficial de organismo internacional do qual o Brasil seja membro'), (b'29', '29 - Servi\xe7o Militar - Afastamento tempor\xe1rio para prestar servi\xe7o militar obrigat\xf3rio;'), (b'30', '30 - Suspens\xe3o disciplinar - CLT, art. 474'), (b'31', '31 - Servidor P\xfablico em Disponibilidade'), (b'33', '33 - Licen\xe7a Maternidade - de 180 dias, Lei 13.301/2016.'), (b'34', '34 - Inatividade do trabalhador avulso (portu\xe1rio ou n\xe3o portu\xe1rio) por per\xedodo superior a 90 dias')]),
        ),
        migrations.AlterField(
            model_name='s2200brasil',
            name='tplograd',
            field=models.CharField(max_length=4, choices=[(b'A', 'A - \xc1rea'), (b'A', 'A - \xc1rea'), (b'A V', 'A V - \xc1rea Verde'), (b'A V', 'A V - \xc1rea Verde'), (b'AC', 'AC - Acesso'), (b'AC', 'AC - Acesso'), (b'ACA', 'ACA - Acampamento'), (b'ACA', 'ACA - Acampamento'), (b'ACL', 'ACL - Acesso Local'), (b'ACL', 'ACL - Acesso Local'), (b'AD', 'AD - Adro'), (b'AD', 'AD - Adro'), (b'AE', 'AE - \xc1rea Especial'), (b'AE', 'AE - \xc1rea Especial'), (b'AER', 'AER - Aeroporto'), (b'AER', 'AER - Aeroporto'), (b'AL', 'AL - Alameda'), (b'AL', 'AL - Alameda'), (b'AMD', 'AMD - Avenida Marginal Direita'), (b'AMD', 'AMD - Avenida Marginal Direita'), (b'AME', 'AME - Avenida Marginal Esquerda'), (b'AME', 'AME - Avenida Marginal Esquerda'), (b'AN', 'AN - Anel Vi\xe1rio'), (b'AN', 'AN - Anel Vi\xe1rio'), (b'ANT', 'ANT - Antiga Estrada'), (b'ANT', 'ANT - Antiga Estrada'), (b'ART', 'ART - Art\xe9ria'), (b'ART', 'ART - Art\xe9ria'), (b'AT', 'AT - Alto'), (b'AT', 'AT - Alto'), (b'ATL', 'ATL - Atalho'), (b'ATL', 'ATL - Atalho'), (b'AV', 'AV - Avenida'), (b'AV', 'AV - Avenida'), (b'AVC', 'AVC - Avenida Contorno'), (b'AVC', 'AVC - Avenida Contorno'), (b'AVM', 'AVM - Avenida Marginal'), (b'AVM', 'AVM - Avenida Marginal'), (b'AVV', 'AVV - Avenida Velha'), (b'AVV', 'AVV - Avenida Velha'), (b'BAL', 'BAL - Balne\xe1rio'), (b'BAL', 'BAL - Balne\xe1rio'), (b'BC', 'BC - Beco'), (b'BC', 'BC - Beco'), (b'BCO', 'BCO - Buraco'), (b'BCO', 'BCO - Buraco'), (b'BEL', 'BEL - Belvedere'), (b'BEL', 'BEL - Belvedere'), (b'BL', 'BL - Bloco'), (b'BL', 'BL - Bloco'), (b'BLO', 'BLO - Bal\xe3o'), (b'BLO', 'BLO - Bal\xe3o'), (b'BLS', 'BLS - Blocos'), (b'BLS', 'BLS - Blocos'), (b'BLV', 'BLV - Bulevar'), (b'BLV', 'BLV - Bulevar'), (b'BSQ', 'BSQ - Bosque'), (b'BSQ', 'BSQ - Bosque'), (b'BVD', 'BVD - Boulevard'), (b'BVD', 'BVD - Boulevard'), (b'BX', 'BX - Baixa'), (b'BX', 'BX - Baixa'), (b'C', 'C - Cais'), (b'C', 'C - Cais'), (b'CAL', 'CAL - Cal\xe7ada'), (b'CAL', 'CAL - Cal\xe7ada'), (b'CAM', 'CAM - Caminho'), (b'CAM', 'CAM - Caminho'), (b'CAN', 'CAN - Canal'), (b'CAN', 'CAN - Canal'), (b'CH', 'CH - Ch\xe1cara'), (b'CH', 'CH - Ch\xe1cara'), (b'CHA', 'CHA - Chapad\xe3o'), (b'CHA', 'CHA - Chapad\xe3o'), (b'CIC', 'CIC - Ciclovia'), (b'CIC', 'CIC - Ciclovia'), (b'CIR', 'CIR - Circular'), (b'CIR', 'CIR - Circular'), (b'CJ', 'CJ - Conjunto'), (b'CJ', 'CJ - Conjunto'), (b'CJM', 'CJM - Conjunto Mutir\xe3o'), (b'CJM', 'CJM - Conjunto Mutir\xe3o'), (b'CMP', 'CMP - Complexo Vi\xe1rio'), (b'CMP', 'CMP - Complexo Vi\xe1rio'), (b'COL', 'COL - Col\xf4nia'), (b'COL', 'COL - Col\xf4nia'), (b'COM', 'COM - Comunidade'), (b'COM', 'COM - Comunidade'), (b'CON', 'CON - Condom\xednio'), (b'CON', 'CON - Condom\xednio'), (b'COR', 'COR - Corredor'), (b'COR', 'COR - Corredor'), (b'CPO', 'CPO - Campo'), (b'CPO', 'CPO - Campo'), (b'CRG', 'CRG - C\xf3rrego'), (b'CRG', 'CRG - C\xf3rrego'), (b'CTN', 'CTN - Contorno'), (b'CTN', 'CTN - Contorno'), (b'DSC', 'DSC - Descida'), (b'DSC', 'DSC - Descida'), (b'DSV', 'DSV - Desvio'), (b'DSV', 'DSV - Desvio'), (b'DT', 'DT - Distrito'), (b'DT', 'DT - Distrito'), (b'EB', 'EB - Entre Bloco'), (b'EB', 'EB - Entre Bloco'), (b'EIM', 'EIM - Estrada Intermunicipal'), (b'EIM', 'EIM - Estrada Intermunicipal'), (b'ENS', 'ENS - Enseada'), (b'ENS', 'ENS - Enseada'), (b'ENT', 'ENT - Entrada Particular'), (b'ENT', 'ENT - Entrada Particular'), (b'EQ', 'EQ - Entre Quadra'), (b'EQ', 'EQ - Entre Quadra'), (b'ESC', 'ESC - Escada'), (b'ESC', 'ESC - Escada'), (b'ESD', 'ESD - Escadaria'), (b'ESD', 'ESD - Escadaria'), (b'ESE', 'ESE - Estrada Estadual'), (b'ESE', 'ESE - Estrada Estadual'), (b'ESI', 'ESI - Estrada Vicinal'), (b'ESI', 'ESI - Estrada Vicinal'), (b'ESL', 'ESL - Estrada de Liga\xe7\xe3o'), (b'ESL', 'ESL - Estrada de Liga\xe7\xe3o'), (b'ESM', 'ESM - Estrada Municipal'), (b'ESM', 'ESM - Estrada Municipal'), (b'ESP', 'ESP - Esplanada'), (b'ESP', 'ESP - Esplanada'), (b'ESS', 'ESS - Estrada de Servid\xe3o'), (b'ESS', 'ESS - Estrada de Servid\xe3o'), (b'EST', 'EST - Estrada'), (b'EST', 'EST - Estrada'), (b'ESV', 'ESV - Estrada Velha'), (b'ESV', 'ESV - Estrada Velha'), (b'ETA', 'ETA - Estrada Antiga'), (b'ETA', 'ETA - Estrada Antiga'), (b'ETC', 'ETC - Esta\xe7\xe3o'), (b'ETC', 'ETC - Esta\xe7\xe3o'), (b'ETD', 'ETD - Est\xe1dio'), (b'ETD', 'ETD - Est\xe1dio'), (b'ETN', 'ETN - Est\xe2ncia'), (b'ETN', 'ETN - Est\xe2ncia'), (b'ETP', 'ETP - Estrada Particular'), (b'ETP', 'ETP - Estrada Particular'), (b'ETT', 'ETT - Estacionamento'), (b'ETT', 'ETT - Estacionamento'), (b'EVA', 'EVA - Evang\xe9lica'), (b'EVA', 'EVA - Evang\xe9lica'), (b'EVD', 'EVD - Elevada'), (b'EVD', 'EVD - Elevada'), (b'EX', 'EX - Eixo Industrial'), (b'EX', 'EX - Eixo Industrial'), (b'FAV', 'FAV - Favela'), (b'FAV', 'FAV - Favela'), (b'FAZ', 'FAZ - Fazenda'), (b'FAZ', 'FAZ - Fazenda'), (b'FER', 'FER - Ferrovia'), (b'FER', 'FER - Ferrovia'), (b'FNT', 'FNT - Fonte'), (b'FNT', 'FNT - Fonte'), (b'FRA', 'FRA - Feira'), (b'FRA', 'FRA - Feira'), (b'FTE', 'FTE - Forte'), (b'FTE', 'FTE - Forte'), (b'GAL', 'GAL - Galeria'), (b'GAL', 'GAL - Galeria'), (b'GJA', 'GJA - Granja'), (b'GJA', 'GJA - Granja'), (b'HAB', 'HAB - N\xfacleo Habitacional'), (b'HAB', 'HAB - N\xfacleo Habitacional'), (b'IA', 'IA - Ilha'), (b'IA', 'IA - Ilha'), (b'IND', 'IND - Indeterminado'), (b'IND', 'IND - Indeterminado'), (b'IOA', 'IOA - Ilhota'), (b'IOA', 'IOA - Ilhota'), (b'JD', 'JD - Jardim'), (b'JD', 'JD - Jardim'), (b'JDE', 'JDE - Jardinete'), (b'JDE', 'JDE - Jardinete'), (b'LD', 'LD - Ladeira'), (b'LD', 'LD - Ladeira'), (b'LGA', 'LGA - Lagoa'), (b'LGA', 'LGA - Lagoa'), (b'LGO', 'LGO - Lago'), (b'LGO', 'LGO - Lago'), (b'LOT', 'LOT - Loteamento'), (b'LOT', 'LOT - Loteamento'), (b'LRG', 'LRG - Largo'), (b'LRG', 'LRG - Largo'), (b'LT', 'LT - Lote'), (b'LT', 'LT - Lote'), (b'MER', 'MER - Mercado'), (b'MER', 'MER - Mercado'), (b'MNA', 'MNA - Marina'), (b'MNA', 'MNA - Marina'), (b'MOD', 'MOD - Modulo'), (b'MOD', 'MOD - Modulo'), (b'MRG', 'MRG - Proje\xe7\xe3o'), (b'MRG', 'MRG - Proje\xe7\xe3o'), (b'MRO', 'MRO - Morro'), (b'MRO', 'MRO - Morro'), (b'MTE', 'MTE - Monte'), (b'MTE', 'MTE - Monte'), (b'NUC', 'NUC - N\xfacleo'), (b'NUC', 'NUC - N\xfacleo'), (b'NUR', 'NUR - N\xfacleo Rural'), (b'NUR', 'NUR - N\xfacleo Rural'), (b'OUT', 'OUT - Outeiro'), (b'OUT', 'OUT - Outeiro'), (b'PAR', 'PAR - Paralela'), (b'PAR', 'PAR - Paralela'), (b'PAS', 'PAS - Passeio'), (b'PAS', 'PAS - Passeio'), (b'PAT', 'PAT - P\xe1tio'), (b'PAT', 'PAT - P\xe1tio'), (b'PC', 'PC - Pra\xe7a'), (b'PC', 'PC - Pra\xe7a'), (b'PCE', 'PCE - Pra\xe7a de Esportes'), (b'PCE', 'PCE - Pra\xe7a de Esportes'), (b'PDA', 'PDA - Parada'), (b'PDA', 'PDA - Parada'), (b'PDO', 'PDO - Paradouro'), (b'PDO', 'PDO - Paradouro'), (b'PNT', 'PNT - Ponta'), (b'PNT', 'PNT - Ponta'), (b'PR', 'PR - Praia'), (b'PR', 'PR - Praia'), (b'PRL', 'PRL - Prolongamento'), (b'PRL', 'PRL - Prolongamento'), (b'PRM', 'PRM - Parque Municipal'), (b'PRM', 'PRM - Parque Municipal'), (b'PRQ', 'PRQ - Parque'), (b'PRQ', 'PRQ - Parque'), (b'PRR', 'PRR - Parque Residencial'), (b'PRR', 'PRR - Parque Residencial'), (b'PSA', 'PSA - Passarela'), (b'PSA', 'PSA - Passarela'), (b'PSG', 'PSG - Passagem'), (b'PSG', 'PSG - Passagem'), (b'PSP', 'PSP - Passagem de Pedestre'), (b'PSP', 'PSP - Passagem de Pedestre'), (b'PSS', 'PSS - Passagem Subterr\xe2nea'), (b'PSS', 'PSS - Passagem Subterr\xe2nea'), (b'PTE', 'PTE - Ponte'), (b'PTE', 'PTE - Ponte'), (b'PTO', 'PTO - Porto'), (b'PTO', 'PTO - Porto'), (b'Q', 'Q - Quadra'), (b'Q', 'Q - Quadra'), (b'QTA', 'QTA - Quinta'), (b'QTA', 'QTA - Quinta'), (b'QTS', 'QTS - Quintas'), (b'QTS', 'QTS - Quintas'), (b'R', 'R - Rua'), (b'R', 'R - Rua'), (b'R I', 'R I - Rua Integra\xe7\xe3o'), (b'R I', 'R I - Rua Integra\xe7\xe3o'), (b'R L', 'R L - Rua de Liga\xe7\xe3o'), (b'R L', 'R L - Rua de Liga\xe7\xe3o'), (b'R P', 'R P - Rua Particular'), (b'R P', 'R P - Rua Particular'), (b'R V', 'R V - Rua Velha'), (b'R V', 'R V - Rua Velha'), (b'RAM', 'RAM - Ramal'), (b'RAM', 'RAM - Ramal'), (b'RCR', 'RCR - Recreio'), (b'RCR', 'RCR - Recreio'), (b'REC', 'REC - Recanto'), (b'REC', 'REC - Recanto'), (b'RER', 'RER - Retiro'), (b'RER', 'RER - Retiro'), (b'RES', 'RES - Residencial'), (b'RES', 'RES - Residencial'), (b'RET', 'RET - Reta'), (b'RET', 'RET - Reta'), (b'RLA', 'RLA - Ruela'), (b'RLA', 'RLA - Ruela'), (b'RMP', 'RMP - Rampa'), (b'RMP', 'RMP - Rampa'), (b'ROA', 'ROA - Rodo Anel'), (b'ROA', 'ROA - Rodo Anel'), (b'ROD', 'ROD - Rodovia'), (b'ROD', 'ROD - Rodovia'), (b'ROT', 'ROT - Rotula'), (b'ROT', 'ROT - Rotula'), (b'RPE', 'RPE - Rua de Pedestre'), (b'RPE', 'RPE - Rua de Pedestre'), (b'RPR', 'RPR - Margem'), (b'RPR', 'RPR - Margem'), (b'RTN', 'RTN - Retorno'), (b'RTN', 'RTN - Retorno'), (b'RTT', 'RTT - Rotat\xf3ria'), (b'RTT', 'RTT - Rotat\xf3ria'), (b'SEG', 'SEG - Segunda Avenida'), (b'SEG', 'SEG - Segunda Avenida'), (b'SIT', 'SIT - Sitio'), (b'SIT', 'SIT - Sitio'), (b'SRV', 'SRV - Servid\xe3o'), (b'SRV', 'SRV - Servid\xe3o'), (b'ST', 'ST - Setor'), (b'ST', 'ST - Setor'), (b'SUB', 'SUB - Subida'), (b'SUB', 'SUB - Subida'), (b'TCH', 'TCH - Trincheira'), (b'TCH', 'TCH - Trincheira'), (b'TER', 'TER - Terminal'), (b'TER', 'TER - Terminal'), (b'TR', 'TR - Trecho'), (b'TR', 'TR - Trecho'), (b'TRV', 'TRV - Trevo'), (b'TRV', 'TRV - Trevo'), (b'TUN', 'TUN - T\xfanel'), (b'TUN', 'TUN - T\xfanel'), (b'TV', 'TV - Travessa'), (b'TV', 'TV - Travessa'), (b'TVP', 'TVP - Travessa Particular'), (b'TVP', 'TVP - Travessa Particular'), (b'TVV', 'TVV - Travessa Velha'), (b'TVV', 'TVV - Travessa Velha'), (b'UNI', 'UNI - Unidade'), (b'UNI', 'UNI - Unidade'), (b'V', 'V - Via'), (b'V', 'V - Via'), (b'V C', 'V C - Via Coletora'), (b'V C', 'V C - Via Coletora'), (b'V L', 'V L - Via Local'), (b'V L', 'V L - Via Local'), (b'V-E', 'V-E - Via Expressa'), (b'V-E', 'V-E - Via Expressa'), (b'VAC', 'VAC - Via de Acesso'), (b'VAC', 'VAC - Via de Acesso'), (b'VAL', 'VAL - Vala'), (b'VAL', 'VAL - Vala'), (b'VCO', 'VCO - Via Costeira'), (b'VCO', 'VCO - Via Costeira'), (b'VD', 'VD - Viaduto'), (b'VD', 'VD - Viaduto'), (b'VER', 'VER - Vereda'), (b'VER', 'VER - Vereda'), (b'VEV', 'VEV - Via Elevado'), (b'VEV', 'VEV - Via Elevado'), (b'VL', 'VL - Vila'), (b'VL', 'VL - Vila'), (b'VLA', 'VLA - Viela'), (b'VLA', 'VLA - Viela'), (b'VLE', 'VLE - Vale'), (b'VLE', 'VLE - Vale'), (b'VLT', 'VLT - Via Litor\xe2nea'), (b'VLT', 'VLT - Via Litor\xe2nea'), (b'VPE', 'VPE - Via de Pedestre'), (b'VPE', 'VPE - Via de Pedestre'), (b'VRT', 'VRT - Variante'), (b'VRT', 'VRT - Variante'), (b'ZIG', 'ZIG - Zigue-Zague'), (b'ZIG', 'ZIG - Zigue-Zague')]),
        ),
        migrations.AlterField(
            model_name='s2200dependente',
            name='tpdep',
            field=models.CharField(max_length=2, choices=[(b'01', '01 - C\xf4njuge'), (b'02', '02 - Companheiro(a) com o(a) qual tenha filho ou viva h\xe1 mais de 5 (cinco) anos ou possua Declara\xe7\xe3o de Uni\xe3o Est\xe1vel'), (b'03', '03 - Filho(a) ou enteado(a)'), (b'04', '04 - Filho(a) ou enteado(a), universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xba grau'), (b'06', '06 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'), (b'07', '07 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xb0 grau, do(a) qual detenha a guarda judicial'), (b'09', '09 - Pais, av\xf3s e bisav\xf3s'), (b'10', '10 - Menor pobre do qual detenha a guarda judicial'), (b'11', '11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'), (b'12', '12 - Ex-c\xf4njuge'), (b'99', '99 - Agregado/Outros')]),
        ),
        migrations.AlterField(
            model_name='s2200exterior',
            name='paisresid',
            field=models.CharField(max_length=3, choices=[(b'008', '008 - Abu Dhabi'), (b'009', '009 - Dirce'), (b'013', '013 - Afeganistao'), (b'017', '017 - Albania, Republica Da'), (b'020', '020 - Alboran-Perejil,Ilhas'), (b'023', '023 - Alemanha'), (b'025', '025 - Alemanha, Republica Democratica'), (b'031', '031 - Burkina Faso'), (b'037', '037 - Andorra'), (b'040', '040 - Angola'), (b'041', '041 - Anguilla'), (b'043', '043 - Antigua E Barbuda'), (b'047', '047 - Antilhas Holandesas'), (b'053', '053 - Arabia Saudita'), (b'059', '059 - Argelia'), (b'063', '063 - Argentina'), (b'064', '064 - Armenia, Republica Da'), (b'065', '065 - Aruba'), (b'069', '069 - Australia'), (b'072', '072 - Austria'), (b'073', '073 - Azerbaijao, Republica Do'), (b'077', '077 - Bahamas, Ilhas'), (b'080', '080 - Bahrein, Ilhas'), (b'081', '081 - Bangladesh'), (b'083', '083 - Barbados'), (b'085', '085 - Belarus, Republica Da'), (b'087', '087 - Belgica'), (b'088', '088 - Belize'), (b'090', '090 - Bermudas'), (b'093', '093 - Mianmar (BIRMANIA)'), (b'097', '097 - Bolivia, Estado Plurinacional Da'), (b'098', '098 - Bosnia-Herzegovina (REPUBLICA Da)'), (b'100', '100 - Int.Z.F.Manaus'), (b'101', '101 - Botsuana'), (b'105', '105 - Brasil'), (b'106', '106 - Fretado P/Brasil'), (b'108', '108 - Brunei'), (b'111', '111 - Bulgaria, Republica Da'), (b'115', '115 - Burundi'), (b'119', '119 - Butao'), (b'127', '127 - Cabo Verde, Republica De'), (b'131', '131 - Cachemira'), (b'137', '137 - Cayman, Ilhas'), (b'141', '141 - Camboja'), (b'145', '145 - Camaroes'), (b'149', '149 - Canada'), (b'150', '150 - Jersey, Ilha Do Canal'), (b'151', '151 - Canarias, Ilhas'), (b'152', '152 - Canal,Ilhas'), (b'153', '153 - Cazaquistao, Republica Do'), (b'154', '154 - Catar'), (b'158', '158 - Chile'), (b'160', '160 - China, Republica Popular'), (b'161', '161 - Formosa (TAIWAN)'), (b'163', '163 - Chipre'), (b'165', '165 - Cocos(Keeling),Ilhas'), (b'169', '169 - Colombia'), (b'173', '173 - Comores, Ilhas'), (b'177', '177 - Congo'), (b'183', '183 - Cook, Ilhas'), (b'187', '187 - Coreia (DO Norte), Rep.Pop.Democratica'), (b'190', '190 - Coreia (DO Sul), Republica Da'), (b'193', '193 - Costa Do Marfim'), (b'195', '195 - Croacia (REPUBLICA Da)'), (b'196', '196 - Costa Rica'), (b'198', '198 - Coveite'), (b'199', '199 - Cuba'), (b'229', '229 - Benin'), (b'232', '232 - Dinamarca'), (b'235', '235 - Dominica,Ilha'), (b'237', '237 - Dubai'), (b'239', '239 - Equador'), (b'240', '240 - Egito'), (b'243', '243 - Eritreia'), (b'244', '244 - Emirados Arabes Unidos'), (b'245', '245 - Espanha'), (b'246', '246 - Eslovenia, Republica Da'), (b'247', '247 - Eslovaca, Republica'), (b'249', '249 - Estados Unidos'), (b'251', '251 - Estonia, Republica Da'), (b'253', '253 - Etiopia'), (b'255', '255 - Falkland (ILHAS Malvinas)'), (b'259', '259 - Feroe, Ilhas'), (b'263', '263 - Fezzan'), (b'267', '267 - Filipinas'), (b'271', '271 - Finlandia'), (b'275', '275 - Franca'), (b'281', '281 - Gabao'), (b'285', '285 - Gambia'), (b'289', '289 - Gana'), (b'291', '291 - Georgia, Republica Da'), (b'293', '293 - Gibraltar'), (b'297', '297 - Granada'), (b'301', '301 - Grecia'), (b'305', '305 - Groenlandia'), (b'309', '309 - Guadalupe'), (b'313', '313 - Guam'), (b'317', '317 - Guatemala'), (b'325', '325 - Guiana Francesa'), (b'329', '329 - Guine'), (b'331', '331 - Guine-Equatorial'), (b'334', '334 - Guine-Bissau'), (b'337', '337 - Guiana'), (b'341', '341 - Haiti'), (b'345', '345 - Honduras'), (b'351', '351 - Hong Kong'), (b'355', '355 - Hungria, Republica Da'), (b'357', '357 - Iemen'), (b'358', '358 - Iemem Do Sul'), (b'359', '359 - Man, Ilha De'), (b'361', '361 - India'), (b'365', '365 - Indonesia'), (b'367', '367 - Inglaterra'), (b'369', '369 - Iraque'), (b'372', '372 - Ira, Republica Islamica Do'), (b'375', '375 - Irlanda'), (b'379', '379 - Islandia'), (b'383', '383 - Israel'), (b'386', '386 - Italia'), (b'388', '388 - Servia E Montenegro'), (b'391', '391 - Jamaica'), (b'395', '395 - Jammu'), (b'396', '396 - Johnston, Ilhas'), (b'399', '399 - Japao'), (b'403', '403 - Jordania'), (b'411', '411 - Kiribati'), (b'420', '420 - Laos, Rep.Pop.Democr.Do'), (b'423', '423 - Lebuan,Ilhas'), (b'426', '426 - Lesoto'), (b'427', '427 - Letonia, Republica Da'), (b'431', '431 - Libano'), (b'434', '434 - Liberia'), (b'438', '438 - Libia'), (b'440', '440 - Liechtenstein'), (b'442', '442 - Lituania, Republica Da'), (b'445', '445 - Luxemburgo'), (b'447', '447 - Macau'), (b'449', '449 - Macedonia, Ant.Rep.Iugoslava'), (b'450', '450 - Madagascar'), (b'452', '452 - Ilha Da Madeira'), (b'455', '455 - Malasia'), (b'458', '458 - Malavi'), (b'461', '461 - Maldivas'), (b'464', '464 - Mali'), (b'467', '467 - Malta'), (b'472', '472 - Marianas Do Norte'), (b'474', '474 - Marrocos'), (b'476', '476 - Marshall,Ilhas'), (b'477', '477 - Martinica'), (b'485', '485 - Mauricio'), (b'488', '488 - Mauritania'), (b'490', '490 - Midway, Ilhas'), (b'493', '493 - Mexico'), (b'494', '494 - Moldavia, Republica Da'), (b'495', '495 - Monaco'), (b'497', '497 - Mongolia'), (b'499', '499 - Micronesia'), (b'501', '501 - Montserrat,Ilhas'), (b'505', '505 - Mocambique'), (b'507', '507 - Namibia'), (b'508', '508 - Nauru'), (b'511', '511 - Christmas,Ilha (NAVIDAD)'), (b'517', '517 - Nepal'), (b'521', '521 - Nicaragua'), (b'525', '525 - Niger'), (b'528', '528 - Nigeria'), (b'531', '531 - Niue,Ilha'), (b'535', '535 - Norfolk,Ilha'), (b'538', '538 - Noruega'), (b'542', '542 - Nova Caledonia'), (b'545', '545 - Papua Nova Guine'), (b'548', '548 - Nova Zelandia'), (b'551', '551 - Vanuatu'), (b'556', '556 - Oma'), (b'563', '563 - Pacifico,Ilhas Do (ADMINISTRACAO Dos Eua)'), (b'566', '566 - Pacifico,Ilhas Do (POSSESSAO Dos Eua)'), (b'569', '569 - Pacifico,Ilhas Do (TERRITORIO Em Fideicomisso Dos'), (b'573', '573 - Paises Baixos (HOLANDA)'), (b'575', '575 - Palau'), (b'576', '576 - Paquistao'), (b'578', '578 - Palestina'), (b'580', '580 - Panama'), (b'583', '583 - Papua Nova Guin\xe9'), (b'586', '586 - Paraguai'), (b'589', '589 - Peru'), (b'593', '593 - Pitcairn,Ilha'), (b'599', '599 - Polinesia Francesa'), (b'603', '603 - Polonia, Republica Da'), (b'607', '607 - Portugal'), (b'611', '611 - Porto Rico'), (b'623', '623 - Quenia'), (b'625', '625 - Quirguiz, Republica'), (b'628', '628 - Reino Unido'), (b'640', '640 - Republica Centro-Africana'), (b'647', '647 - Republica Dominicana'), (b'660', '660 - Reuniao, Ilha'), (b'665', '665 - Zimbabue'), (b'670', '670 - Romenia'), (b'675', '675 - Ruanda'), (b'676', '676 - Russia, Federacao Da'), (b'677', '677 - Salomao, Ilhas'), (b'678', '678 - Saint Kitts E Nevis'), (b'685', '685 - Saara Ocidental'), (b'687', '687 - El Salvador'), (b'690', '690 - Samoa'), (b'691', '691 - Samoa Americana'), (b'695', '695 - Sao Cristovao E Neves,Ilhas'), (b'697', '697 - San Marino'), (b'700', '700 - Sao Pedro E Miquelon'), (b'705', '705 - Sao Vicente E Granadinas'), (b'710', '710 - Santa Helena'), (b'715', '715 - Santa Lucia'), (b'720', '720 - Sao Tome E Principe, Ilhas'), (b'728', '728 - Senegal'), (b'731', '731 - Seychelles'), (b'735', '735 - Serra Leoa'), (b'738', '738 - Sikkim'), (b'741', '741 - Cingapura'), (b'744', '744 - Siria, Republica Arabe Da'), (b'748', '748 - Somalia'), (b'750', '750 - Sri Lanka'), (b'754', '754 - Suazilandia'), (b'756', '756 - Africa Do Sul'), (b'759', '759 - Sudao'), (b'764', '764 - Suecia'), (b'767', '767 - Suica'), (b'770', '770 - Suriname'), (b'772', '772 - Tadjiquistao, Republica Do'), (b'776', '776 - Tailandia'), (b'780', '780 - Tanzania, Rep.Unida Da'), (b'782', '782 - Territorio Brit.Oc.Indico'), (b'783', '783 - Djibuti'), (b'785', '785 - Territorio da Alta Comissao do Pacifico Ocidental'), (b'788', '788 - Chade'), (b'790', '790 - Tchecoslovaquia'), (b'791', '791 - Tcheca, Republica'), (b'795', '795 - Timor Leste'), (b'800', '800 - Togo'), (b'805', '805 - Toquelau,Ilhas'), (b'810', '810 - Tonga'), (b'815', '815 - Trinidad E Tobago'), (b'820', '820 - Tunisia'), (b'823', '823 - Turcas E Caicos,Ilhas'), (b'824', '824 - Turcomenistao, Republica Do'), (b'827', '827 - Turquia'), (b'828', '828 - Tuvalu'), (b'831', '831 - Ucrania'), (b'833', '833 - Uganda'), (b'840', '840 - Uniao Das Republicas Socialistas Sovieticas'), (b'845', '845 - Uruguai'), (b'847', '847 - Uzbequistao, Republica Do'), (b'848', '848 - Vaticano, Est.Da Cidade Do'), (b'850', '850 - Venezuela'), (b'855', '855 - Vietname Norte'), (b'858', '858 - Vietna'), (b'863', '863 - Virgens,Ilhas (BRITANICAS)'), (b'866', '866 - Virgens,Ilhas (E.U.A.)'), (b'870', '870 - Fiji'), (b'873', '873 - Wake, Ilha'), (b'875', '875 - Wallis E Futuna, Ilhas'), (b'888', '888 - Congo, Republica Democratica Do'), (b'890', '890 - Zambia')]),
        ),
        migrations.AlterField(
            model_name='s2200localtrabdom',
            name='tplograd',
            field=models.CharField(max_length=4, choices=[(b'A', 'A - \xc1rea'), (b'A', 'A - \xc1rea'), (b'A V', 'A V - \xc1rea Verde'), (b'A V', 'A V - \xc1rea Verde'), (b'AC', 'AC - Acesso'), (b'AC', 'AC - Acesso'), (b'ACA', 'ACA - Acampamento'), (b'ACA', 'ACA - Acampamento'), (b'ACL', 'ACL - Acesso Local'), (b'ACL', 'ACL - Acesso Local'), (b'AD', 'AD - Adro'), (b'AD', 'AD - Adro'), (b'AE', 'AE - \xc1rea Especial'), (b'AE', 'AE - \xc1rea Especial'), (b'AER', 'AER - Aeroporto'), (b'AER', 'AER - Aeroporto'), (b'AL', 'AL - Alameda'), (b'AL', 'AL - Alameda'), (b'AMD', 'AMD - Avenida Marginal Direita'), (b'AMD', 'AMD - Avenida Marginal Direita'), (b'AME', 'AME - Avenida Marginal Esquerda'), (b'AME', 'AME - Avenida Marginal Esquerda'), (b'AN', 'AN - Anel Vi\xe1rio'), (b'AN', 'AN - Anel Vi\xe1rio'), (b'ANT', 'ANT - Antiga Estrada'), (b'ANT', 'ANT - Antiga Estrada'), (b'ART', 'ART - Art\xe9ria'), (b'ART', 'ART - Art\xe9ria'), (b'AT', 'AT - Alto'), (b'AT', 'AT - Alto'), (b'ATL', 'ATL - Atalho'), (b'ATL', 'ATL - Atalho'), (b'AV', 'AV - Avenida'), (b'AV', 'AV - Avenida'), (b'AVC', 'AVC - Avenida Contorno'), (b'AVC', 'AVC - Avenida Contorno'), (b'AVM', 'AVM - Avenida Marginal'), (b'AVM', 'AVM - Avenida Marginal'), (b'AVV', 'AVV - Avenida Velha'), (b'AVV', 'AVV - Avenida Velha'), (b'BAL', 'BAL - Balne\xe1rio'), (b'BAL', 'BAL - Balne\xe1rio'), (b'BC', 'BC - Beco'), (b'BC', 'BC - Beco'), (b'BCO', 'BCO - Buraco'), (b'BCO', 'BCO - Buraco'), (b'BEL', 'BEL - Belvedere'), (b'BEL', 'BEL - Belvedere'), (b'BL', 'BL - Bloco'), (b'BL', 'BL - Bloco'), (b'BLO', 'BLO - Bal\xe3o'), (b'BLO', 'BLO - Bal\xe3o'), (b'BLS', 'BLS - Blocos'), (b'BLS', 'BLS - Blocos'), (b'BLV', 'BLV - Bulevar'), (b'BLV', 'BLV - Bulevar'), (b'BSQ', 'BSQ - Bosque'), (b'BSQ', 'BSQ - Bosque'), (b'BVD', 'BVD - Boulevard'), (b'BVD', 'BVD - Boulevard'), (b'BX', 'BX - Baixa'), (b'BX', 'BX - Baixa'), (b'C', 'C - Cais'), (b'C', 'C - Cais'), (b'CAL', 'CAL - Cal\xe7ada'), (b'CAL', 'CAL - Cal\xe7ada'), (b'CAM', 'CAM - Caminho'), (b'CAM', 'CAM - Caminho'), (b'CAN', 'CAN - Canal'), (b'CAN', 'CAN - Canal'), (b'CH', 'CH - Ch\xe1cara'), (b'CH', 'CH - Ch\xe1cara'), (b'CHA', 'CHA - Chapad\xe3o'), (b'CHA', 'CHA - Chapad\xe3o'), (b'CIC', 'CIC - Ciclovia'), (b'CIC', 'CIC - Ciclovia'), (b'CIR', 'CIR - Circular'), (b'CIR', 'CIR - Circular'), (b'CJ', 'CJ - Conjunto'), (b'CJ', 'CJ - Conjunto'), (b'CJM', 'CJM - Conjunto Mutir\xe3o'), (b'CJM', 'CJM - Conjunto Mutir\xe3o'), (b'CMP', 'CMP - Complexo Vi\xe1rio'), (b'CMP', 'CMP - Complexo Vi\xe1rio'), (b'COL', 'COL - Col\xf4nia'), (b'COL', 'COL - Col\xf4nia'), (b'COM', 'COM - Comunidade'), (b'COM', 'COM - Comunidade'), (b'CON', 'CON - Condom\xednio'), (b'CON', 'CON - Condom\xednio'), (b'COR', 'COR - Corredor'), (b'COR', 'COR - Corredor'), (b'CPO', 'CPO - Campo'), (b'CPO', 'CPO - Campo'), (b'CRG', 'CRG - C\xf3rrego'), (b'CRG', 'CRG - C\xf3rrego'), (b'CTN', 'CTN - Contorno'), (b'CTN', 'CTN - Contorno'), (b'DSC', 'DSC - Descida'), (b'DSC', 'DSC - Descida'), (b'DSV', 'DSV - Desvio'), (b'DSV', 'DSV - Desvio'), (b'DT', 'DT - Distrito'), (b'DT', 'DT - Distrito'), (b'EB', 'EB - Entre Bloco'), (b'EB', 'EB - Entre Bloco'), (b'EIM', 'EIM - Estrada Intermunicipal'), (b'EIM', 'EIM - Estrada Intermunicipal'), (b'ENS', 'ENS - Enseada'), (b'ENS', 'ENS - Enseada'), (b'ENT', 'ENT - Entrada Particular'), (b'ENT', 'ENT - Entrada Particular'), (b'EQ', 'EQ - Entre Quadra'), (b'EQ', 'EQ - Entre Quadra'), (b'ESC', 'ESC - Escada'), (b'ESC', 'ESC - Escada'), (b'ESD', 'ESD - Escadaria'), (b'ESD', 'ESD - Escadaria'), (b'ESE', 'ESE - Estrada Estadual'), (b'ESE', 'ESE - Estrada Estadual'), (b'ESI', 'ESI - Estrada Vicinal'), (b'ESI', 'ESI - Estrada Vicinal'), (b'ESL', 'ESL - Estrada de Liga\xe7\xe3o'), (b'ESL', 'ESL - Estrada de Liga\xe7\xe3o'), (b'ESM', 'ESM - Estrada Municipal'), (b'ESM', 'ESM - Estrada Municipal'), (b'ESP', 'ESP - Esplanada'), (b'ESP', 'ESP - Esplanada'), (b'ESS', 'ESS - Estrada de Servid\xe3o'), (b'ESS', 'ESS - Estrada de Servid\xe3o'), (b'EST', 'EST - Estrada'), (b'EST', 'EST - Estrada'), (b'ESV', 'ESV - Estrada Velha'), (b'ESV', 'ESV - Estrada Velha'), (b'ETA', 'ETA - Estrada Antiga'), (b'ETA', 'ETA - Estrada Antiga'), (b'ETC', 'ETC - Esta\xe7\xe3o'), (b'ETC', 'ETC - Esta\xe7\xe3o'), (b'ETD', 'ETD - Est\xe1dio'), (b'ETD', 'ETD - Est\xe1dio'), (b'ETN', 'ETN - Est\xe2ncia'), (b'ETN', 'ETN - Est\xe2ncia'), (b'ETP', 'ETP - Estrada Particular'), (b'ETP', 'ETP - Estrada Particular'), (b'ETT', 'ETT - Estacionamento'), (b'ETT', 'ETT - Estacionamento'), (b'EVA', 'EVA - Evang\xe9lica'), (b'EVA', 'EVA - Evang\xe9lica'), (b'EVD', 'EVD - Elevada'), (b'EVD', 'EVD - Elevada'), (b'EX', 'EX - Eixo Industrial'), (b'EX', 'EX - Eixo Industrial'), (b'FAV', 'FAV - Favela'), (b'FAV', 'FAV - Favela'), (b'FAZ', 'FAZ - Fazenda'), (b'FAZ', 'FAZ - Fazenda'), (b'FER', 'FER - Ferrovia'), (b'FER', 'FER - Ferrovia'), (b'FNT', 'FNT - Fonte'), (b'FNT', 'FNT - Fonte'), (b'FRA', 'FRA - Feira'), (b'FRA', 'FRA - Feira'), (b'FTE', 'FTE - Forte'), (b'FTE', 'FTE - Forte'), (b'GAL', 'GAL - Galeria'), (b'GAL', 'GAL - Galeria'), (b'GJA', 'GJA - Granja'), (b'GJA', 'GJA - Granja'), (b'HAB', 'HAB - N\xfacleo Habitacional'), (b'HAB', 'HAB - N\xfacleo Habitacional'), (b'IA', 'IA - Ilha'), (b'IA', 'IA - Ilha'), (b'IND', 'IND - Indeterminado'), (b'IND', 'IND - Indeterminado'), (b'IOA', 'IOA - Ilhota'), (b'IOA', 'IOA - Ilhota'), (b'JD', 'JD - Jardim'), (b'JD', 'JD - Jardim'), (b'JDE', 'JDE - Jardinete'), (b'JDE', 'JDE - Jardinete'), (b'LD', 'LD - Ladeira'), (b'LD', 'LD - Ladeira'), (b'LGA', 'LGA - Lagoa'), (b'LGA', 'LGA - Lagoa'), (b'LGO', 'LGO - Lago'), (b'LGO', 'LGO - Lago'), (b'LOT', 'LOT - Loteamento'), (b'LOT', 'LOT - Loteamento'), (b'LRG', 'LRG - Largo'), (b'LRG', 'LRG - Largo'), (b'LT', 'LT - Lote'), (b'LT', 'LT - Lote'), (b'MER', 'MER - Mercado'), (b'MER', 'MER - Mercado'), (b'MNA', 'MNA - Marina'), (b'MNA', 'MNA - Marina'), (b'MOD', 'MOD - Modulo'), (b'MOD', 'MOD - Modulo'), (b'MRG', 'MRG - Proje\xe7\xe3o'), (b'MRG', 'MRG - Proje\xe7\xe3o'), (b'MRO', 'MRO - Morro'), (b'MRO', 'MRO - Morro'), (b'MTE', 'MTE - Monte'), (b'MTE', 'MTE - Monte'), (b'NUC', 'NUC - N\xfacleo'), (b'NUC', 'NUC - N\xfacleo'), (b'NUR', 'NUR - N\xfacleo Rural'), (b'NUR', 'NUR - N\xfacleo Rural'), (b'OUT', 'OUT - Outeiro'), (b'OUT', 'OUT - Outeiro'), (b'PAR', 'PAR - Paralela'), (b'PAR', 'PAR - Paralela'), (b'PAS', 'PAS - Passeio'), (b'PAS', 'PAS - Passeio'), (b'PAT', 'PAT - P\xe1tio'), (b'PAT', 'PAT - P\xe1tio'), (b'PC', 'PC - Pra\xe7a'), (b'PC', 'PC - Pra\xe7a'), (b'PCE', 'PCE - Pra\xe7a de Esportes'), (b'PCE', 'PCE - Pra\xe7a de Esportes'), (b'PDA', 'PDA - Parada'), (b'PDA', 'PDA - Parada'), (b'PDO', 'PDO - Paradouro'), (b'PDO', 'PDO - Paradouro'), (b'PNT', 'PNT - Ponta'), (b'PNT', 'PNT - Ponta'), (b'PR', 'PR - Praia'), (b'PR', 'PR - Praia'), (b'PRL', 'PRL - Prolongamento'), (b'PRL', 'PRL - Prolongamento'), (b'PRM', 'PRM - Parque Municipal'), (b'PRM', 'PRM - Parque Municipal'), (b'PRQ', 'PRQ - Parque'), (b'PRQ', 'PRQ - Parque'), (b'PRR', 'PRR - Parque Residencial'), (b'PRR', 'PRR - Parque Residencial'), (b'PSA', 'PSA - Passarela'), (b'PSA', 'PSA - Passarela'), (b'PSG', 'PSG - Passagem'), (b'PSG', 'PSG - Passagem'), (b'PSP', 'PSP - Passagem de Pedestre'), (b'PSP', 'PSP - Passagem de Pedestre'), (b'PSS', 'PSS - Passagem Subterr\xe2nea'), (b'PSS', 'PSS - Passagem Subterr\xe2nea'), (b'PTE', 'PTE - Ponte'), (b'PTE', 'PTE - Ponte'), (b'PTO', 'PTO - Porto'), (b'PTO', 'PTO - Porto'), (b'Q', 'Q - Quadra'), (b'Q', 'Q - Quadra'), (b'QTA', 'QTA - Quinta'), (b'QTA', 'QTA - Quinta'), (b'QTS', 'QTS - Quintas'), (b'QTS', 'QTS - Quintas'), (b'R', 'R - Rua'), (b'R', 'R - Rua'), (b'R I', 'R I - Rua Integra\xe7\xe3o'), (b'R I', 'R I - Rua Integra\xe7\xe3o'), (b'R L', 'R L - Rua de Liga\xe7\xe3o'), (b'R L', 'R L - Rua de Liga\xe7\xe3o'), (b'R P', 'R P - Rua Particular'), (b'R P', 'R P - Rua Particular'), (b'R V', 'R V - Rua Velha'), (b'R V', 'R V - Rua Velha'), (b'RAM', 'RAM - Ramal'), (b'RAM', 'RAM - Ramal'), (b'RCR', 'RCR - Recreio'), (b'RCR', 'RCR - Recreio'), (b'REC', 'REC - Recanto'), (b'REC', 'REC - Recanto'), (b'RER', 'RER - Retiro'), (b'RER', 'RER - Retiro'), (b'RES', 'RES - Residencial'), (b'RES', 'RES - Residencial'), (b'RET', 'RET - Reta'), (b'RET', 'RET - Reta'), (b'RLA', 'RLA - Ruela'), (b'RLA', 'RLA - Ruela'), (b'RMP', 'RMP - Rampa'), (b'RMP', 'RMP - Rampa'), (b'ROA', 'ROA - Rodo Anel'), (b'ROA', 'ROA - Rodo Anel'), (b'ROD', 'ROD - Rodovia'), (b'ROD', 'ROD - Rodovia'), (b'ROT', 'ROT - Rotula'), (b'ROT', 'ROT - Rotula'), (b'RPE', 'RPE - Rua de Pedestre'), (b'RPE', 'RPE - Rua de Pedestre'), (b'RPR', 'RPR - Margem'), (b'RPR', 'RPR - Margem'), (b'RTN', 'RTN - Retorno'), (b'RTN', 'RTN - Retorno'), (b'RTT', 'RTT - Rotat\xf3ria'), (b'RTT', 'RTT - Rotat\xf3ria'), (b'SEG', 'SEG - Segunda Avenida'), (b'SEG', 'SEG - Segunda Avenida'), (b'SIT', 'SIT - Sitio'), (b'SIT', 'SIT - Sitio'), (b'SRV', 'SRV - Servid\xe3o'), (b'SRV', 'SRV - Servid\xe3o'), (b'ST', 'ST - Setor'), (b'ST', 'ST - Setor'), (b'SUB', 'SUB - Subida'), (b'SUB', 'SUB - Subida'), (b'TCH', 'TCH - Trincheira'), (b'TCH', 'TCH - Trincheira'), (b'TER', 'TER - Terminal'), (b'TER', 'TER - Terminal'), (b'TR', 'TR - Trecho'), (b'TR', 'TR - Trecho'), (b'TRV', 'TRV - Trevo'), (b'TRV', 'TRV - Trevo'), (b'TUN', 'TUN - T\xfanel'), (b'TUN', 'TUN - T\xfanel'), (b'TV', 'TV - Travessa'), (b'TV', 'TV - Travessa'), (b'TVP', 'TVP - Travessa Particular'), (b'TVP', 'TVP - Travessa Particular'), (b'TVV', 'TVV - Travessa Velha'), (b'TVV', 'TVV - Travessa Velha'), (b'UNI', 'UNI - Unidade'), (b'UNI', 'UNI - Unidade'), (b'V', 'V - Via'), (b'V', 'V - Via'), (b'V C', 'V C - Via Coletora'), (b'V C', 'V C - Via Coletora'), (b'V L', 'V L - Via Local'), (b'V L', 'V L - Via Local'), (b'V-E', 'V-E - Via Expressa'), (b'V-E', 'V-E - Via Expressa'), (b'VAC', 'VAC - Via de Acesso'), (b'VAC', 'VAC - Via de Acesso'), (b'VAL', 'VAL - Vala'), (b'VAL', 'VAL - Vala'), (b'VCO', 'VCO - Via Costeira'), (b'VCO', 'VCO - Via Costeira'), (b'VD', 'VD - Viaduto'), (b'VD', 'VD - Viaduto'), (b'VER', 'VER - Vereda'), (b'VER', 'VER - Vereda'), (b'VEV', 'VEV - Via Elevado'), (b'VEV', 'VEV - Via Elevado'), (b'VL', 'VL - Vila'), (b'VL', 'VL - Vila'), (b'VLA', 'VLA - Viela'), (b'VLA', 'VLA - Viela'), (b'VLE', 'VLE - Vale'), (b'VLE', 'VLE - Vale'), (b'VLT', 'VLT - Via Litor\xe2nea'), (b'VLT', 'VLT - Via Litor\xe2nea'), (b'VPE', 'VPE - Via de Pedestre'), (b'VPE', 'VPE - Via de Pedestre'), (b'VRT', 'VRT - Variante'), (b'VRT', 'VRT - Variante'), (b'ZIG', 'ZIG - Zigue-Zague'), (b'ZIG', 'ZIG - Zigue-Zague')]),
        ),
    ]
