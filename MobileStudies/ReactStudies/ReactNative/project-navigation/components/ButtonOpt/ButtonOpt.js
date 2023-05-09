
import { StyleSheet, Text, View, Button, Image, TouchableOpacity } from 'react-native';

export function ButtonOpt(props) {
  return(
    <View style={styles.container}>
        <TouchableOpacity style={styles.medicineTouchable} onPress={props.func}>
            <Image style={styles.img} source={props.source}></Image>
            <Text style={styles.text}>{props.title}</Text>
        </TouchableOpacity>
    </View>
    );
}

const styles = StyleSheet.create({
    container: {
        shadowColor: '#000000',
        shadowOffset: {width: 0, height: 5},
        shadowOpacity: 0.20,
        shadowRadius: 3,
    },
    img:{
        width: 38,
        height: 38,
        marginRight: 5,
    },
    medicineTouchable:{
        textAlign: 'center',
        display: 'flex',
        flexDirection: 'row',
        marginTop: '15%',
        backgroundColor: '#F6F6F6',
        padding: 15,
        borderRadius: 5,

    },
    text:{
        textAlign:'center',
        color: '#741B47', 
        fontFamily: 'serif',
        fontWeight: 'bold',
        marginTop: '4%',
        marginLeft: '1%',
    },
})