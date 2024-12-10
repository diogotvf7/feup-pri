import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"
import type { article } from "types"
import nlp from "compromise";
 
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export const article_to_url = (article: article) => {
  return article.title.toLowerCase().replace(/ /g, '-') + '-' + article.id
}

export const stock_change_color = (value : number) => {
  const toHex = (component: number): string =>
    component.toString(16).padStart(2, '0');

  const intensity = Math.floor((Math.abs(value) / 5) * 255);
  
  if (value >= 5) {
    return "#00FF00";
  } else if (value <= -5) {
    return "#FF0000";
  } else if (value > 0) {
    const greenComponent = 255 - intensity;
    return `#${toHex(greenComponent)}FF${toHex(greenComponent)}`;    
  } else if (value < 0) {
    const redComponent = 255 - intensity;
    return `#FF${toHex(redComponent)}${toHex(redComponent)}`;
  }
}

export const get_date = (date: string) => {
  if (!date) return ''
  const d = new Date(date)
  return d.toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
}

export const split_paragraphs = (text : string) => {
  const doc = nlp(text);
  return doc.sentences().out('array'); 
}
