// 'use client';

// import { useState } from "react";

// class logginInfo {
//     email: string;
//     password: string;

//     constructor(email: string, password: string) {
//         this.email = email;
//         this.password = password;
//     }

//     toJson() {
//         return { email: this.email, password: this.password };
//     }
// }
// // const [user, setUser] = useState<logginInfo | null>(null);

// function handleSubmit(email: string, password: string) {
//     setUser(new logginInfo(email, password));
// }

// function getToJson() {
//     if (user) {
//         return user.toJson();
//     }
//     return null;
// }

// export { handleSubmit, getToJson };