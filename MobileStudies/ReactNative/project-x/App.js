import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image} from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <View style={styles.containertitle}>
        <Image style={styles.imagemenu} source={require("./assets/menu-aberto.png")}></Image>
        <Text style={styles.title}>@guifreitads</Text>
      </View>
      <View style={styles.containertext}>
        <View>
          <Text style={styles.textf}>Hello, some people call me Guilherme, i think that's right!</Text>
          <Text style={styles.textf}>I'm on the way to become a Full-Stack developer and i'm trying to learn some React Native</Text>
        </View>
      </View>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#6600dd',
    alignItems: "center"
  },

  containertitle:{
    marginTop: 50,
    alignItems: "center"
  },

  imagemenu: {
    display: 'flex',
    width: 50,
    height: 50
  },

  title:{
    fontSize: 30,
    fontWeight: "bold",
    color: "#fff"
  },

  containertext: {
    marginTop: 30,
    alignItems: "center",
    marginLeft: 20,
    marginRight: 20
  },
  textf: {
    fontSize: 18,
    color: 'white',
    textAlign: 'justify'
  }
});
