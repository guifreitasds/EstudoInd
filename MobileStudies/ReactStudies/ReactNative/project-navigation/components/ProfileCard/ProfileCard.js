import { StyleSheet, View, Text, Image } from "react-native";

export function ProfileCard(props) {
    return(
        <View style={styles.container}>
            <View style={styles.containerHead}>
                <Image source={require('../../assets/COROA-nofill.png')} style={styles.image}></Image>
                <Text style={styles.textName}>Valricéia do Carmo</Text>
            </View>
        </View>
    );
}

const styles = StyleSheet.create({
    container:{
        alignItems: 'center',
        marginTop: '6%',
    },
    containerHead:{
        alignItems: 'center',
    },
    image:{
        width: 100,
        height: 100,
    },
    textName: {
        fontSize: 28,
        fontFamily: 'serif',
    }
})