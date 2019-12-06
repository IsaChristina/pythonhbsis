terminal = ['Piloto', 'Oficial 1', 'Oficial 2', 'Chefe', 'Comissária 1', 'Comissária 2', 'Presidiário', 'Policial']
aviao = []

def ida(motorista, passageiro):
    print('--- IDA ---')
    print(f'Terminal: {terminal}')
    terminal.remove(motorista)    
    terminal.remove(passageiro)
    aviao.append(motorista)                 
    aviao.append(passageiro)
    print(f'Ida para o avião - Motorista: {motorista} | Passageiro: {passageiro}')
    print('*'*20)

def volta(motorista):
    print('--- VOLTA ---')
    print(f'Avião: {aviao}')
    aviao.remove(motorista)
    terminal.append(motorista)
    print(f'Volta para o terminal - Motorista: {motorista}')
    print('*'*20)
    
