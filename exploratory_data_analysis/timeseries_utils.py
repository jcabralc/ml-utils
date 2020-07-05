def testa_estacionaridade(serie):
    
    ### Calcula estatísticas móveis ### 
    rolmean = serie.rolling(window = 12).mean()
    rolstd = serie.rolling(window = 12).std()

    # Plot das estatísticas móveis
    orig = plt.plot(serie, color = 'blue', label = 'Original')
    mean = plt.plot(rolmean, color = 'red', label = 'Média Móvel')
    std = plt.plot(rolstd, color = 'black', label = 'Desvio Padrão')
    plt.legend(loc = 'best')
    plt.title('Estatísticas Móveis - Média e Desvio Padrão')
    plt.show()
    
    
    ### Plots ACF e PACF ### 
    plt.rcParams.update({'figure.figsize': (16,10)})

    # Plot do gráfico ACF
    # https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_acf.html
    plt.subplot(211)
    plot_acf(serie, ax = plt.gca(), lags = 30)

    # Plot do gráfico PACF
    # https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_pacf.html
    plt.subplot(212)
    plot_pacf(serie, ax = plt.gca(), lags = 30)
    plt.show()
    
    ### Teste Dickey-Fuller: ### 
    print('\nResultado do Teste Dickey-Fuller:\n')
    # Teste
    dfteste = adfuller(serie, autolag = 'AIC')
    # Formatando a saída
    dfsaida = pd.Series(dfteste[0:4], index = ['Estatística do Teste',
                                               'Valor-p',
                                               'Número de Lags Consideradas',
                                               'Número de Observações Usadas'])
    # Loop por cada item da saída do teste
    for key, value in dfteste[4].items():
        dfsaida['Valor Crítico (%s)'%key] = value

    # Print
    print (dfsaida)
    
    # Testa o valor-p
    print ('\nConclusão:')
    if dfsaida[1] > 0.05:
        print('\nO valor-p é maior que 0.05 e, portanto, não temos evidências para rejeitar a hipótese nula.')
        print('Essa série provavelmente não é estacionária.')
    else:
        print('\nO valor-p é menor que 0.05 e, portanto, temos evidências para rejeitar a hipótese nula.')
        print('Essa série provavelmente é estacionária.')

def decomposicao_serie(serie):
    # Multiplicative Decomposition 
    decomposicao_multiplicativa = sm.tsa.seasonal_decompose(serie, model = 'multiplicative', 
                                                            extrapolate_trend = 'freq')

    # Additive Decomposition
    decomposicao_aditiva = sm.tsa.seasonal_decompose(serie, model = 'aditive', 
                                                     extrapolate_trend = 'freq')
    # Definir extrapolate_trend = 'freq' cuida de todos os valores ausentes na tendência e nos 
    # resíduos no início da série (se existirem).
    # Plot
    plt.rcParams.update({'figure.figsize': (16,10)})
    decomposicao_multiplicativa.plot().suptitle('Decomposição Multiplicativa', fontsize = 22)
    decomposicao_aditiva.plot().suptitle('Decomposição Aditiva', fontsize = 22)
    plt.show()
