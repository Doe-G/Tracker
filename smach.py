import rospy
import smach

def Detectar(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                            outcomes=['detecta', 'no_detecta'],
                            input_keys=['image_in'],
                            output_keys=['person_data_out'])
    
    def execute(self, stateData):
        pass

def PideAyuda(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                            outcomes=['reintenta'])
    
    def execute(self, stateData):
        pass

def ExtraccionCaracteristicas(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                            outcomes=['manda_posicion'],
                            input_keys=['person_data_in', 'image_in'],
                            output_keys=['person_data_out'])
    
    def execute(self, stateData):
        pass

def PublicarPosicion(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                            outcomes=['siguiente_frame'],
                            input_keys=['position_in'])
    
    def execute(self, stateData):
        pass

def QueryNext(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                            outcomes=['actualiza_data', 'manda_posicion', 'reidentifica'],
                            input_keys=['person_data_in'],
                            output_keys=['image_out'])
    
    def execute(self, stateData):
        pass

def Reidentificacion(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                            outcomes=['actualiza_data'],
                            input_keys=['image_in', 'person_data_in'],
                            output_keys=['image_out', 'person_data_out'])
    
    def execute(self, stateData):
        pass

def main():

    sm = smach.StateMachine(outcomes=['kill'])

    with sm:
        smach.StateMachine.add('Dectar', Detectar(),
                                transitions=[])
    
    outcome = sm.execute()