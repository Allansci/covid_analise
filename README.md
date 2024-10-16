# Visualização de Dados da COVID-19 para Estados Brasileiros

Este projeto é uma aplicação web simples baseada em Streamlit que oferece visualizações dos dados da COVID-19 para diferentes estados do Brasil. Os usuários podem selecionar um estado específico e escolher qual dado desejam visualizar, como novos casos, novos óbitos, óbitos por 100 mil habitantes ou casos por 100 mil habitantes. Os dados são apresentados em um gráfico de linha, permitindo que os usuários acompanhem facilmente as tendências ao longo do tempo.

## Funcionalidades

- **Seleção de Estado**: Os usuários podem escolher qualquer estado brasileiro para visualizar.
- **Seleção de Tipo de Dado**: A aplicação permite alternar entre diferentes tipos de dados da COVID-19:
  - Novos Casos
  - Novos Óbitos
  - Óbitos por 100 mil Habitantes
  - Casos por 100 mil Habitantes
- **Gráfico Interativo**: O gráfico é atualizado automaticamente com base na seleção do usuário, proporcionando uma experiência clara e interativa.
- **Design Responsivo**: O layout da aplicação se adapta a diferentes tamanhos de tela, garantindo que funcione tanto em desktops quanto em dispositivos móveis.

## Como Funciona

1. **Fonte de Dados**: A aplicação obtém seus dados de um dataset público hospedado no GitHub, contendo as últimas estatísticas da COVID-19 para os estados brasileiros.
2. **Interação do Usuário**: Os usuários interagem com uma interface simples, onde podem selecionar o estado e o tipo de dado que desejam visualizar. Isso faz com que a aplicação busque e exiba o gráfico correspondente.
3. **Plotagem do Gráfico**: Os dados são visualizados utilizando o Plotly, com o gráfico mostrando a tendência da métrica de COVID-19 escolhida para o estado selecionado ao longo do tempo.

## Instalação e Execução da Aplicação

### Requisitos

- **Python 3.x**
- **Streamlit**: Framework web para aplicações interativas.
- **Plotly**: Para criar gráficos dinâmicos.

Para rodar a aplicação localmente, siga estes passos:

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-repo/covid19-data-visualization.git
cd covid19-data-visualization
```
