
import { StyleSheet, Text, View, Button, Image } from 'react-native';

export function TextAndSubText() {
  return(
    <View>
        <Text style={styles.textMain}>Vamos Começar a usar o <Text style={{color: '#741B47'}}>C.O.R.O.A!</Text></Text>
        <Text style={styles.subTextMain}>O que você gostaria de fazer por aqui?</Text>
    </View>
    );
}

const styles = StyleSheet.create({
    textMain:{
        fontFamily: 'serif',
        fontSize: 32,
        fontWeight: 'bold',
        textAlign: 'center',
    },
    subTextMain:{
        marginTop: '10%',
        fontSize: 16,
        marginLeft: '2%'
    }
})