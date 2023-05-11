import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native'
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { HomeScreen} from './screens/home'
import { MedicinesScreen } from './screens/medicines';
import Ionicons from 'react-native-vector-icons/Ionicons'
import { ProfileScreen } from './screens/profile';

const Stack = createNativeStackNavigator();
const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator
        screenOptions={({ route }) => ({
          tabBarIcon: ({ focused, color, size }) => {
            let iconName;

            if (route.name === 'Home') {
              iconName = focused
                ? 'home'
                : 'home-outline';
            } else if (route.name === 'Medicines') {
              iconName = focused ? 'medkit' : 'medkit-outline';
            } else if (route.name === 'Profile') {
              iconName = focused ? 'people' : 'people-outline';
            }

            // You can return any component that you like here!
            return <Ionicons name={iconName} size={size} color={color} />;
          },
          tabBarActiveTintColor: '#741B47',
          tabBarInactiveTintColor: 'gray',
        })}>
        <Tab.Screen name='Home' component={HomeScreen}/>
        <Tab.Screen name='Medicines' component={MedicinesScreen}/>
        <Tab.Screen name='Profile' component={ProfileScreen}/>
      </Tab.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',  
    alignItems: 'center',
    justifyContent: 'center',
  },
});
