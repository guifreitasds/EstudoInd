
import { StyleSheet, Text, View, Button, Image, TouchableOpacity } from 'react-native';

export function ButtonOpt(props) {
  return(
    <View style={styles.container}>
        <TouchableOpacity style={styles.medicineTouchable}>
            <Image style={styles.img} source={props.source}></Image>
            <Text style={styles.text}>{props.title}</Text>
        </TouchableOpacity>
    </View>
    );
}

const styles = StyleSheet.create({
    container:{

    },
    img:{
        width: 38,
        height: 38,
    },
    medicineTouchable:{
        display: 'flex',
        flexDirection: 'row',
        marginTop: '15%',
        backgroundColor: '#F6F6F6',
        padding: 25,
        borderRadius: 5,
    },
    text:{
        color: '#741B47', 
        fontFamily: 'serif',
        fontWeight: 'bold',
        marginTop: '4%',
        marginLeft: '3%',
    },
})